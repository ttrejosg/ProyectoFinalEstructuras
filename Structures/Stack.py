from pygame.locals import *

class Stack:

    ''' Creación de la clase anidada en Stack '''
    class Node:
        def __init__(self,value):
            self.value = value
            self.next = None

    ''' Metodo inicializador de la clase Stack '''
    def __init__(self, position):
        self.head = None
        self.tail = None
        self.length = 0
        self.headbox = Rect(position[0], position[1], 200, 600)

    ''' Método que imprime el contenido de la lista simplemente enlazada '''
    def print(self):
        print_sll = []
        current_node = self.head
        while current_node:
            print_sll.append(current_node.value)
            current_node = current_node.next
        print(f'Lista actual: {print_sll}\nCantidad de nodos: {self.length}')

    '''Método que apila un nuevo elemento'''
    def push(self, value):
        new_node = self.Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    '''Método que despila el primer elemento'''
    def pop(self):
        pop_node = self.head
        if self.length <= 1:
            self.head = None
            self.tail = None
        else:
            self.head = pop_node.next
            pop_node.next = None
        self.length -= 1
        return pop_node

    ''' Método que retorna el nodo en la posición indicada de la lista'''
    def get_node(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == self.length - 1:
            return self.tail
        
        current_node = self.head
        counter = 0
        while index != counter:
            current_node = current_node.next
            counter += 1
        return current_node

    ''' Método que retorna el valor del nodo en la posición indicada de la lista'''
    def get_node_value(self, index):
        node = self.get_node(index)
        if node != None: return node.value
        else: print('Index fuera de rango')

    '''Método que se encarga de dibujar la pila'''
    def draw(self, screen):
        index = self.length - 1
        while index >= 0 and self.length != 0:
            card = self.get_node_value(index)
            screen.blit(card.image, card.position)
            index -= 1

    '''Método que se encarga de revisar si el stack tiene todas las cartas y estan ordenadas de menor a mayor'''
    def is_sorted(self):
        i = 1
        index = self.length - 1
        while index >= 0 and self.length != 0:
            card = self.get_node_value(index)
            if card.value == i: i += 1
            index -= 1
        return i == 15
