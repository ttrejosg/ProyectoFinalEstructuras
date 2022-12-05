from collections import defaultdict
import pygame

class BTree():

    class Node():
        ''' Clase inicializzadora del nodo '''
        def __init__(self, value):
            self.left = None
            self.right = None
            self.value = value
            self.position = (675, 120)

    ''' Clase inicializadora del arbol n-ario'''
    def __init__(self):
        self.root = None

    ''' Método de incersion de un nodo de manera balanceada'''
    def insert(self, value):
        def balanced_insertion(root, value, position, level):
            if value < root.value:
                if root.left is None:
                    root.left = self.Node(value)
                    root.left.position = (position[0] - 30 * 2 - level , position[1] + 30 * 2 + 20)
                else: balanced_insertion(root.left, value, root.left.position, level - 17)
            elif value > root.value:
                if root.right is None:
                    root.right = self.Node(value)
                    root.right.position = (position[0] + 30 * 2 + level, position[1] + 30 * 2 + 20)
                else: balanced_insertion(root.right, value, root.right.position, level - 17)

        if value.isdigit():
            if self.root == None: self.root = self.Node(int(value)) 
            else: balanced_insertion(self.root, int(value), self.root.position, 40)

    '''
    Inorder traversal
    Left -> Root -> Right
    '''
    def inorder_traversal(self):
        res = []
        def ino_t(node):
            if node:
                ino_t(node.left)
                res.append(node.value)
                ino_t(node.right)

        ino_t(self.root)
        return res

    '''
    Preorder traversal
    Root -> Left ->Right
    '''
    def preorder_traversal(self):
        res = []
        def pro_t(node):
            if node:
                res.append(node.value)
                pro_t(node.left)
                pro_t(node.right)

        pro_t(self.root)
        return res

    '''
    Postorder traversal
    Left -> Right -> Root
    '''
    def postorder_traversal(self):
        res = []
        def poo_t(node):
            if node:
                poo_t(node.left)
                poo_t(node.right)
                res.append(node.value)

        poo_t(self.root)
        return res

    '''
    Lever_order_traversal
    Por niveles
    '''
    def level_order_traversal(self):
        route = defaultdict(list) # Crea el manejador de datos

        def dfs(node, level): # Funcion encargada de añadir los valores al manejador
            if node != None:
                route[level].append(node.value)
                dfs(node.left, level+1)
                dfs(node.right, level+1) 

        dfs(self.root, 0)
        return [ans for k,ans in sorted(route.items())] 

    '''Método que se encarga de dibujar el arbol binario'''
    def draw(self, screen):
        def dlot(node, screen): # Funcion encargada de añadir los valores al manejador
            if node != None:
                pygame.draw.circle(screen, (17, 219, 106), (node.position[0], node.position[1]), 30, 0)
                pygame.draw.circle(screen, (7, 9, 42), (node.position[0], node.position[1]), 30, 2)

                if node.left != None: 
                    pygame.draw.line(screen, (17, 219, 106), (node.position[0], node.position[1]), 
                                                                (node.left.position[0], node.left.position[1]), 5)
                    dlot(node.left, screen)
                if node.right != None: 
                    pygame.draw.line(screen, (17, 219, 106), (node.position[0], node.position[1]), 
                                                                (node.right.position[0], node.right.position[1]), 5)
                    dlot(node.right, screen) 

                text_surface = pygame.font.SysFont('Corbel', 35).render(str(node.value), True, (7, 9, 42))
                screen.blit(text_surface, (node.position[0] - 10, node.position[1] - 20))

        dlot(self.root,screen)