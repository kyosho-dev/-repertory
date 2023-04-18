from itertools import count
from turtle import st

import PySimpleGUI as sg

#inporta o meu codigo 

import layout_estilo
import layout_função



class Tela:

     def __init__(self):

        #layout

        layout = layout_estilo.Pagina_1
        
        #cria a janela
        self.janela = sg.Window("RPG romura").layout(layout)

        
     def Iniciar(self):
        while True:

          layout_função.fc.menu_1(self)



