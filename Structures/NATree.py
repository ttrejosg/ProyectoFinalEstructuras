from collections import defaultdict
import pygame

class NAryTree():

    class Node():
        ''' Clase inicializzadora del nodo '''
        def __init__(self, value, parent) -> None:
            self.value = value
            self.child = []
            self.parent = parent
            self.position = (450, 120)

    ''' Clase inicializadora del arbol n-ario'''
    def __init__(self):
        self.root = None
        self.radio = 40
    
    def insert(self, parent, value):
        if not self.root:
            self.root = self.Node(value, None)
            self.root.parent = self.root
            return True
        elif self.non_equals(self.root, value): return self.insert_child(self.root, parent, value)
        else: return False

    ''' Método de incersion de un nodo '''
    def insert_child(self, root: Node, parent, value):
        if root.value == parent:
            root.child.append(self.Node(value, root))
            return True
        else:
            for i in range(len(root.child)):
                if self.insert_child(root.child[i], parent, value): return True

    ''' Método que valida la existencia previa de un nodo buscado '''
    def non_equals(self, root: Node, value):
        if root.value == value: return False
        for c in root.child:
            if c.value == value: return False
            elif not self.non_equals(c, value): return False
        return True
        
    ''' Recorre un arbol N-Ario de forma recursiva en base a su profundidad '''    
    def level_order_traversal(self):
        route = defaultdict(list) # Crea el manejador de datos

        def dfs(node, level): # Funcion encargada de añadir los valores al manejador
            route[level].append(node)
            for child in node.child: 
                dfs(child,level+1) # LLamado recursivo p[or cada hijo

        dfs(self.root, 0) # Primer llamado
        return [ans for k,ans in sorted(route.items())] 

    '''Se encarga de dibujar el arbol n-ario en pantalla'''
    def draw(self, screen):
        tree = self.level_order_traversal()
        y = 80 + self.radio
        if  y + 20 + (len(tree) * self.radio * 2) > 600: self.radio -= 10
        for level in tree:
            x = ((1350 - ((self.radio *2* len(level)) + ((len(level) - 1) * 10))) / 2) + self.radio
            for node in level:
                pygame.draw.circle(screen, (17, 219, 106), (x, y), self.radio, 0)
                pygame.draw.circle(screen, (7, 9, 42), (x, y), self.radio, 2)
                pygame.draw.line(screen, (17, 219, 106), node.parent.position, (x, y), 5)
                node.position = (x, y)
                text_surface = pygame.font.SysFont('Corbel', 35).render(node.value, True, (7, 9, 42))
                screen.blit(text_surface, (x - 10, y - 20))
                x += self.radio * 2 + 10
            y += self.radio * 2 + 20
