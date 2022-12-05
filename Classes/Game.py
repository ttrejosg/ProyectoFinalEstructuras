import pygame
import sys
import json
from pygame.locals import *
from Structures.Stack import Stack
from Classes.Card import Card
from Classes.Botton import Botton
from Classes.Input import Input
from Structures.NATree import NAryTree
from Structures.BTree import BTree
from Structures.Graph import Graph
from Classes.ComboBox import ComboBox

class Game:

    '''Constructor de la clase Game - Donde se declaran las variables'''
    def __init__(self):
        self.screen = None; self.width = 1350; self.height = 700; self.botton_back = None; self.font = None
        self.pila_botton = None; self.n_arbol_botton = None; self.b_arbol_button = None; self.grafo_botton = None #Botones
        self.stacks = []; self.card = None #Atributos necesarios para la funcionalidad de la pila
        self.add_botton = None; self.value_n_input = None; self.parent_input = None ; self.n_tree = NAryTree(); #Atributos necesarios para la funcionalidad del n-arbol
        self.insert_botton = None; self.value_b_input = None; self.b_tree = BTree(); self.combo_box_tree = None; self.route = None #Atributos necesarios para la funcionalidad del b-arbol
        self.graph = Graph(); self.combo_box_origin = None; self.combo_box_destiny = None; self.weighted = None
        self.set_botton = None; self.dijkstra = None; self.shortest_route = None

        self.background = pygame.transform.scale(pygame.image.load('Images/background.jpg'), (self.width, self.height))
        self.stack_background = pygame.image.load('Images/stack_background.jpg')
        self.win_background = pygame.transform.scale(pygame.image.load('Images/win.jpg'), (self.width, self.height))
        self.tree_background = pygame.transform.scale(pygame.image.load('Images/tree_background.png'), (self.width, self.height))
        self.map = pygame.transform.scale(pygame.image.load('Images/map.png'), (self.width / 2, 640))

    '''GameLoop del juego'''
    def gameLoop(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
                if  event.type == pygame.KEYDOWN:
                    self.validate_inputs(event)
                
                if event.type == MOUSEBUTTONDOWN and event.button == 1:  #Valida si hay un evento de mouse y si se presiono el botton izquierdo
                    if self.botton_back.active: self.button_clicked()
                    elif self.botton_back.box.collidepoint(pygame.mouse.get_pos()): self.back()

                    if self.pila_botton.active:
                        if self.card == None: self.picked_card()
                        else: self.put_card()

                    if self.n_arbol_botton.active:
                        if self.add_botton.box.collidepoint(pygame.mouse.get_pos()): self.add_node()
                    
                    if self.b_arbol_botton.active:
                        if self.insert_botton.box.collidepoint(pygame.mouse.get_pos()): self.insert_node()
                        elif self.combo_box_tree.box.collidepoint(pygame.mouse.get_pos()): self.combo_box_tree.active = True
                        elif self.combo_box_tree.active: self.check_combo_box_tree()

                    if self.grafo_botton.active:
                        if self.combo_box_origin.box.collidepoint(pygame.mouse.get_pos()): self.combo_box_origin.active = True
                        elif self.combo_box_destiny.box.collidepoint(pygame.mouse.get_pos()): self.combo_box_destiny.active = True
                        elif self.combo_box_origin.active: self.combo_box_origin.check()
                        elif self.combo_box_destiny.active: self.combo_box_destiny.check()
                        elif self.set_botton.box.collidepoint(pygame.mouse.get_pos()): self.set_weighted()
                        elif self.dijkstra.box.collidepoint(pygame.mouse.get_pos()): self.dijkstra_function()

            self.draw()
            pygame.display.flip()
            clock.tick(60)

    '''Inicialización del juego'''
    def init_game(self):
        pygame.init()
        self.screen = pygame.display.set_mode([self.width, self.height])
        pygame.display.set_caption('Data Structure')
        icon = pygame.image.load('Images/icon.png')
        pygame.display.set_icon(icon)
        self.font = pygame.font.SysFont('Corbel', 35, False, True)

        self.init_buttons_inputs()
        self.init_combo_box_tree_tree()
        self.init_combo_box_graph()
        self.gameLoop()

    '''Inicialización de los bottones'''
    def init_buttons_inputs(self):
        self.pila_botton = Botton(335, 650, 'Pila', self.font)
        self.n_arbol_botton = Botton(530, 650, 'N-Árbol', self.font)
        self.b_arbol_botton = Botton(725, 650, 'B-Árbol', self.font)
        self.grafo_botton = Botton(920, 650, 'Grafo', self.font)
        self.botton_back = Botton(1200, 650, 'Back', self.font)
        self.botton_back.active = True

        self.parent_input = Input(432, 10, self.font)
        self.value_n_input = Input(632, 10, self.font)
        self.add_botton = Botton(832, 10, 'Add', self.font)

        self.value_b_input = Input(210, 10, self.font)
        self.insert_botton = Botton(330, 10, 'Insert', self.font)
        self.route = Input(500, 10, self.font)

        self.weighted = Input(320, 5, self.font)
        self.set_botton = Botton(430, 5, 'Set Peso', self.font)
        self.dijkstra = Botton(580, 5, 'Dijkstra', self.font)
        self.shortest_route = Input(730, 5, self.font)

    '''Inicialización del comboBox del arbol'''
    def init_combo_box_tree_tree(self):
        comboBox = ['Inorder', 'Postorder', 'Preorder', 'Ampli']
        self.combo_box_tree = ComboBox(50, 10, 'Recorrido', pygame.font.SysFont('Corbel', 25, False, True), comboBox)

    '''Inicialización del comboBox del grafo'''
    def init_combo_box_graph(self):
        comboBox = ['ADZ', 'AXM', 'BAQ', 'BGA', 'BOG', 'CLO', 'CTG', 'CUC', 'CUN', 'GRU', 'LET', 'MDE', 'MTR', 'NVA', 'PEI', 'PSO', 'RCH', 'SMR', 'VUP', 'VVC']
        self.combo_box_origin = ComboBox(20, 5, 'Origen', pygame.font.SysFont('Corbel', 25, False, True), comboBox)
        self.combo_box_destiny = ComboBox(170, 5, 'Destino', pygame.font.SysFont('Corbel', 25, False, True), comboBox)
        
    '''Se encarga de dibujar la pantalla'''
    def draw(self):
        if self.pila_botton.active: self.pila_function()
        elif self.n_arbol_botton.active: self.n_arbol_function()
        elif self.b_arbol_botton.active: self.b_arbol_function()
        elif self.grafo_botton.active: self.grafo_function()
        else: 
            self.screen.blit(self.background, (0, 0))
            self.pila_botton.draw(self.screen)
            self.n_arbol_botton.draw(self.screen)
            self.b_arbol_botton.draw(self.screen)
            self.grafo_botton.draw(self.screen)

    '''Se encarga de revisar si un boton ha sido presionado'''
    def button_clicked(self):
        if self.pila_botton.box.collidepoint(pygame.mouse.get_pos()): 
            self.pila_botton.active = True
            self.stacks.clear()
            self.card = None
            self.load_poker_cards()
            self.botton_back.active = False
            self.n_arbol_botton.active = self.b_arbol_botton.active = self.grafo_botton.active = False
        if self.n_arbol_botton.box.collidepoint(pygame.mouse.get_pos()): 
            self.n_arbol_botton.active = True
            self.botton_back.active = False
            self.pila_botton.active = self.b_arbol_botton.active = self.grafo_botton.active = False
        if self.b_arbol_botton.box.collidepoint(pygame.mouse.get_pos()): 
            self.b_arbol_botton.active = True
            self.botton_back.active = False
            self.pila_botton.active = self.n_arbol_botton.active = self.grafo_botton.active = False
        if self.grafo_botton.box.collidepoint(pygame.mouse.get_pos()): 
            self.grafo_botton.active = True
            self.botton_back.active = False
            self.init_graph()
            self.grafo_function()
            self.pila_botton.active = self.n_arbol_botton.active = self.b_arbol_botton.active = False
    
    '''Método que se encarga de la funcionalidad del boton Pila'''
    def pila_function(self):
        if self.sorted_cards(): self.screen.blit(self.win_background, (0, 0))
        else: 
            self.screen.blit(self.stack_background, (0, 0))
            for stack in self.stacks:
                stack.draw(self.screen)
            if self.card != None: 
                self.card.position = pygame.mouse.get_pos()
                self.screen.blit(self.card.image, self.card.position)
        self.botton_back.draw(self.screen)

    '''Se encarga de revisar si una carta ha sido presionada para ser movida'''
    def picked_card(self):
        for stack in self.stacks:
            if stack.length > 0:
                current_card = stack.head.value
                if current_card.headbox.collidepoint(pygame.mouse.get_pos()):
                    self.card = stack.pop().value
                    break

    '''Se encarga de revisar si cuando se tiene una carta esta se puede colocar en algun stack'''
    def put_card(self):
        for stack in self.stacks:
            if stack.headbox.collidepoint(pygame.mouse.get_pos()):
                if stack.length == 0: 
                    self.card.position = (stack.headbox.x, stack.headbox.y)
                    stack.push(Card(self.card.position, self.card.value))
                    self.card = None
                else: 
                    if stack.head.value.value < self.card.value:
                        self.card.position = (stack.head.value.position[0] + 10, stack.head.value.position[1] + 20)
                        stack.push(Card(self.card.position, self.card.value))
                        self.card = None

    '''Método que se encarga de revisar si algun stack ya esta organizado'''
    def sorted_cards(self):
        for stack in self.stacks:
            if stack.is_sorted(): return True
        return False

    '''Método que se encarga de la funcionalidad del boton Arbol n-ario'''
    def n_arbol_function(self):
        self.screen.blit(self.tree_background, (0, 0))
        self.value_n_input.draw(self.screen)
        self.parent_input.draw(self.screen)
        self.add_botton.draw(self.screen)
        if self.n_tree.root != None: self.n_tree.draw(self.screen)
        self.botton_back.draw(self.screen)

    '''Método que se encarga de agregar un nuevo nodo al Arbol n-ario'''
    def add_node(self):
        self.n_tree.insert(self.parent_input.txt, self.value_n_input.txt)
        self.parent_input.txt = ''
        self.value_n_input.txt = ''

    '''Método que se encarga de validar los inputs del arbol n-ario, actualizandolos'''
    def validate_inputs(self, event):
        if self.n_arbol_botton.active:
            self.value_n_input.validate(event)
            self.parent_input.validate(event)
        elif self.b_arbol_botton.active: self.value_b_input.validate(event)
        elif self.grafo_botton.active: 
            self.weighted.validate(event)
            self.grafo_function()

    '''Método que se encarga de la funcionalidad del boton Arbol binario'''
    def b_arbol_function(self):
        self.screen.blit(self.tree_background, (0, 0))
        self.insert_botton.draw(self.screen)
        self.value_b_input.draw(self.screen)
        self.route.draw(self.screen)
        if self.b_tree.root != None: self.b_tree.draw(self.screen)
        self.combo_box_tree.draw(self.screen)
        self.botton_back.draw(self.screen)

    '''Método que se encarga de insertar un nuevo nodo al Arbol binario'''
    def insert_node(self):
        self.b_tree.insert(self.value_b_input.txt)
        self.value_b_input.txt = ''

    '''Método que se encarga de revisar si se ha seleccionado alguna opcion del comboBox y llevarla acabo'''
    def check_combo_box_tree(self):
        self.combo_box_tree.check()
        if self.combo_box_tree.options[0].active: 
            self.route.txt = str(self.b_tree.inorder_traversal())
            self.combo_box_tree.options[0].active = False
        elif self.combo_box_tree.options[1].active: 
            self.route.txt = str(self.b_tree.postorder_traversal())
            self.combo_box_tree.options[1].active = False
        elif self.combo_box_tree.options[2].active: 
            self.route.txt = str(self.b_tree.preorder_traversal())
            self.combo_box_tree.options[2].active = False
        elif self.combo_box_tree.options[3].active: 
            self.route.txt = str(self.b_tree.level_order_traversal())
            self.combo_box_tree.options[3].active = False

    '''Método que se encarga de la funcionalidad del boton Grafo'''
    def grafo_function(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.map, (300, 60))
        self.weighted.draw(self.screen)
        self.set_botton.draw(self.screen)
        self.dijkstra.draw(self.screen)
        self.shortest_route.draw(self.screen)
        self.graph.draw(self.screen)
        self.combo_box_origin.draw(self.screen)
        self.combo_box_destiny.draw(self.screen)
        self.botton_back.draw(self.screen)

    '''Método que se encarga de setear el peso de una arista o agregar una nueva con su peso'''
    def set_weighted(self):
        for option in self.combo_box_origin.options:
            if option.active: begin = option.txt
        for option in self.combo_box_destiny.options:
            if option.active: end = option.txt
        value = self.weighted.txt
        if value.isdigit(): self.graph.add_edge_special(begin, end, int(value))
        self.weighted.txt = ''

    '''Método que se encarga de la funcionalidad del boton Dijkstra'''
    def dijkstra_function(self):
        begin = -1; end = -1
        for option in self.combo_box_origin.options:
            if option.active: begin = self.graph.index(option.txt)
        for option in self.combo_box_destiny.options:
            if option.active: end = self.graph.index(option.txt)

        if begin != -1 and end != -1:
            result = self.graph.dijkstra(begin, end)
            for i in range(len(result[1])):
                result[1][i] = self.graph.vertices[result[1][i]].value
            self.graph.active_dijkstra = result[1]
            if str(result[0]).isdigit() and len(result[1]) > 1:
                self.shortest_route.txt = str(result[0]) + ' / ' + str(result[1])
            else: self.shortest_route.txt = 'No hay camino'

    '''Método que retorna al menu principal'''
    def back(self):
        self.pila_botton.active = False
        self.n_arbol_botton.active = False
        self.b_arbol_botton.active = False
        self.grafo_botton.active = False
        self.botton_back.active = True

    '''Inicialización de las cartas de poker'''
    def load_poker_cards(self):
        stack1 = Stack((50, 20)); stack2 = Stack((380, 20)); stack3 = Stack((710, 20)); stack4 = Stack((1040, 20))
        stack1.push(Card((50, 20), 10)); stack1.push(Card((60, 40), 12)); stack1.push(Card((70, 60), 5)); stack1.push(Card((80, 80), 3))
        stack2.push(Card((380, 20), 7)); stack2.push(Card((390, 40), 8)); stack2.push(Card((400, 60), 1)); stack2.push(Card((410, 80), 14))
        stack3.push(Card((710, 20), 4)); stack3.push(Card((720, 40), 11)); stack3.push(Card((730, 60), 9)); stack3.push(Card((740, 80), 2))
        stack4.push(Card((1040, 20), 13)); stack4.push(Card((1050, 40), 6))
        self.stacks.append(stack1); self.stacks.append(stack2); self.stacks.append(stack3); self.stacks.append(stack4)

    '''Inicialización del grafo'''
    def init_graph(self):
        with open('ciudades.json') as data:
            ciudades = json.load(data)
            for ciudad in ciudades:
                self.graph.add_vertex(ciudad.get('id'), (ciudad.get('x'), ciudad.get('y')))
            for ciudad in ciudades:
                for destino in ciudad.get('destinations'):
                    self.graph.add_edge(ciudad.get('id'), destino, -1, False)        