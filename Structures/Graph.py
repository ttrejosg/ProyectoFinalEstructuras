import pygame
from math import inf

class Graph:
    class Vertex:
        ''' Clase inicializadora del vertice '''
        def __init__(self, value, position) -> None:
            self.value = value
            self.position = position

    ''' Clase inicializadora del grafo '''
    def __init__(self):
        self.vertices = []
        self.matrix = [[None]*0 for i in range(0)]
        self.active_dijkstra = []

    '''Método que se encarga de añadir un vertice'''
    def add_vertex(self, v, position):
        if self.is_in_vertices(v): return False
        self.vertices.append(self.Vertex(v, position))

        rows = columns = len(self.matrix)
        matrix_aux = [[0] * (rows + 1) for i in range(columns + 1)]
        for f in range(rows):
            for c in range(columns):
                matrix_aux[f][c] = self.matrix[f][c]

        self.matrix = matrix_aux
        return True

    '''Método que se encarga de revisar si el vertice dado ya esta en el grafo'''
    def is_in_vertices(self, v):
        for vertex in self.vertices:
            if v == vertex.value: return True
        return False

    '''Método que se encarga de añadir una arista entre dos vertices con su respectivo peso'''
    def add_edge(self, begin, end, value, directed):
        if not(self.is_in_vertices(begin)) or not(self.is_in_vertices(end)): return False
        else: 
            self.matrix[self.index(begin)][self.index(end)] = value
            if not directed: self.matrix[self.index(end)][self.index(begin)] = value
            else: return True

    '''Método que se encarga de setear el peso de una arista si existe'''
    def add_edge_special(self, begin, end, value):
        if not(self.is_in_vertices(begin)) or not(self.is_in_vertices(end)): return False
        else:
            if self.matrix[self.index(begin)][self.index(end)] != 0:
                self.matrix[self.index(begin)][self.index(end)] = value
                self.matrix[self.index(end)][self.index(begin)] = value

    '''Método que dado el valor de un vertice retorna el index de la lista donde se encuentra'''
    def index(self, v):
        for index in range(len(self.vertices)):
            if v == self.vertices[index].value:
                return index
        return 0

    '''
    Algoritmo de Dijkstra / Calcula la distancia entre dos puntos.
    Cuando solo se le da el de inicio, este calcula la menor distancia entre todo los vertices
    '''
    def dijkstra(self, start, end=-1):
        n = len(self.matrix)
        dist = [inf]*n
        dist[start] = self.matrix[start][start]  # 0
        spVertex = [False]*n
        parent = [-1]*n

        path = [{}]*n

        for count in range(n-1):
            minix = inf
            u = 0
            for v in range(len(spVertex)):
                if spVertex[v] == False and dist[v] <= minix:
                    minix = dist[v]
                    u = v
            spVertex[u] = True
            for v in range(n):
                if not(spVertex[v]) and self.matrix[u][v] > 0 and dist[u] + self.matrix[u][v] < dist[v]:
                    parent[v] = u
                    dist[v] = dist[u] + self.matrix[u][v]

        for i in range(n):
            j = i
            s = []
            while parent[j] != -1:
                s.append(j)
                j = parent[j]
            s.append(start)
            path[i] = s[::-1]
        return (dist[end], path[end]) if end >= 0 else (dist, path)

    '''
    Método que retorna una lista de tuplas, donde cada dupla corresponde a un vertice que es adyacente al 
    vertice dado y el peso de esta arista
    '''
    def get_adjacencies(self, v):
        pos_vertice = self.index(v)
        list_sucesores = []
        for i in range(len(self.matrix)):
            if self.matrix[pos_vertice][i] > 0:
                list_sucesores.append((self.vertices[i], self.matrix[pos_vertice][i]))

        return list_sucesores

    '''Método que se encaga de dibujar el grafo en la pantalla'''
    def draw(self, screen):
        self.draw_aristas(screen)
        self.draw_vertices(screen)

    '''Método que se encaga de dibujar los vertices en la pantalla'''
    def draw_vertices(self, screen):
        for vertex in self.vertices:
            pygame.draw.circle(screen, (0, 0, 0), (vertex.position[0], vertex.position[1]), 1, 0)

    '''Método que se encaga de dibujar las aristas en la pantalla'''
    def draw_aristas(self, screen):
        for vertex in self.vertices:
            aristas = self.get_adjacencies(vertex.value)
            for arista in aristas:
                destiny = arista[0]
                if vertex.value in self.active_dijkstra and destiny.value in self.active_dijkstra:
                    pygame.draw.line(screen, (39, 255, 0), (vertex.position[0], vertex.position[1]), 
                                                                (destiny.position[0], destiny.position[1]), 2)

                else: pygame.draw.line(screen, (0, 0, 0), (vertex.position[0], vertex.position[1]), 
                                                                (destiny.position[0], destiny.position[1]), 2)

                if vertex.position[0] < destiny.position[0]: minx = vertex.position[0]
                else: minx = destiny.position[0]

                if vertex.position[1] < destiny.position[1]: miny = vertex.position[1]
                else: miny = destiny.position[1]

                x = (abs(destiny.position[0] - vertex.position[0]) / 2) + minx
                y = (abs(destiny.position[1] - vertex.position[1]) / 2) + miny

                text_value = pygame.font.SysFont('Corbel', 20, True).render(str(arista[1]), True, (0, 0, 0))
                screen.blit(text_value, (x, y))