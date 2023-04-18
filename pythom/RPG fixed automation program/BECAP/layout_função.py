from itertools import count
from turtle import st

import openpyxl
import random

#pega os dados das clases

import puch


book = openpyxl.load_workbook('Parte da frente.xlsx')


pagina1 = book['Página1']
pagina2 = book['Página2']

##Puchar os valores das classes no documento "lista de classes"

puch.puchar_estatos()

class fc:
    def menu_1(x):
                  #Estrai dados da tela que o usuario clicou / valida apenas paraesse menu
          
          x.Button, x.values = x.janela.Read()
          
          
          #extrai o nome e o lvl

          nome =                x.values['nome']
          lvl =                 int(x.values['Nivel'])

          valor_amarzenado = []

          # COMPARADOR DE PONTOS POR NIVEL


          p_estatus = 0
          p_habilidade = 0 

          if (lvl == 9):
            p_estatus = 6
                 
          if (lvl == 10):
            p_estatus = 8
            
          if (lvl == 13):
            p_estatus = 10
            
          if (lvl == 15):
            p_estatus = 12
            
          if (lvl == 18):
            p_estatus = 14
            
          if (lvl == 20):
            p_estatus = 16
            
          if (lvl == 25):
            p_estatus = 18
       
          if (lvl >= 30):
            p_estatus = 20



          if (lvl == 1):
            p_estatus = 0
            p_habilidade = 0 
        
          if (lvl == 2):
            p_estatus = 0
            p_habilidade = 2 
         
          if (lvl == 3):
            p_estatus = 0
            p_habilidade = 4 

          if (lvl == 4):
            p_estatus = 2
            p_habilidade = 6 
        
          if (lvl == 5):
            p_estatus = 4
            p_habilidade = 10 
        

          if (lvl > 5):
            p_habilidade = 10
            
          cont = lvl - 5
          controle2 = lvl


          while (controle2 > 5): 
                for controle in range(cont):

                    if (controle == 0):
                        p_habilidade = p_habilidade + 2

                    if (controle == 1):
                        p_habilidade = p_habilidade + 2

                    if (controle == 2):
                        p_habilidade = p_habilidade + 2

                    if (controle == 3):
                        p_habilidade = p_habilidade + 4                
                    
                    if (controle == 4):
                        p_habilidade = p_habilidade + 4  

                controle2 = controle2 - 5
                cont = cont - 5

          

          # COMPARADOR DE ATIVAÇÃO


          if (x.values['Mago'] == True):
              valor_amarzenado = puch.Mago_V

          if (x.values['Mago da sorte'] == True):
              valor_amarzenado = puch.Mago_da_sorte_V

          if (x.values['Elementarista'] == True):
              valor_amarzenado = puch.Elementarista_V

          if (x.values['Engenheiro'] == True):
              valor_amarzenado = puch.Engenheiro_V

          if (x.values['Alchemist'] == True):
              valor_amarzenado = puch.Alchemist_V

          if (x.values['Domador'] == True):
              valor_amarzenado = puch.Domador_V

          if (x.values['Arkanoid'] == True):
              valor_amarzenado = puch.Arkanoid_V

          if (x.values['Mestre das almas'] == True):
              valor_amarzenado = puch.Mestre_das_almas_V

          if (x.values['Suporte'] == True):
              valor_amarzenado = puch.Suporte_V

####################################################################################################

          if (x.values['Guerreiro'] == True):
              valor_amarzenado = puch.Guerreiro_V

          if (x.values['Escudeiro'] == True):
              valor_amarzenado = puch.Escudeiro_V

          if (x.values['Brute force warrior'] == True):
              valor_amarzenado = puch.Brute_force_warrior_V

          if (x.values['Barbaro'] == True):
              valor_amarzenado = puch.Barbaro_V

          if (x.values['Guerreiro 2 SW'] == True):
              valor_amarzenado = puch.Guerreiro_2_SW_V

          if (x.values['Guerreiro 2H'] == True):
              valor_amarzenado = puch.Guerreiro_2H_V

          if (x.values['Ceifador'] == True):
              valor_amarzenado = puch.Ceifador_V

          if (x.values['Monje'] == True):
              valor_amarzenado = puch.Monje_V


####################################################################################################

          if (x.values['Arqueiro'] == True):
              valor_amarzenado = puch.Arqueiro_V

          if (x.values['Cruzader'] == True):
              valor_amarzenado = puch.Cruzader_V

####################################################################################################

          if (x.values['Necromance'] == True):
              valor_amarzenado = puch.Necromance_V

          if (x.values['Clerigo'] == True):
              valor_amarzenado = puch.Clerigo_V

          if (x.values['Bardo'] == True):
              valor_amarzenado = puch.Bardo_V

          if (x.values['Orador'] == True):
              valor_amarzenado = puch.Orador_V

          if (x.values['Mediun'] == True):
              valor_amarzenado = puch.Mediun_V

          if (x.values['Druida'] == True):
              valor_amarzenado = puch.Druida_V

####################################################################################################

          if (x.values['Samurai'] == True):
              valor_amarzenado = puch.Samurai_V

          if (x.values['Ninja'] == True):
              valor_amarzenado = puch.Ninja_V

          if (x.values['Ceifeiro'] == True):
              valor_amarzenado = puch.Ceifeiro_V

          if (x.values['Ladino'] == True):
              valor_amarzenado = puch.Ladino_V


          # rola os dados de vida e de mp de acordo com o nivel 
 
          controle3 = lvl
          somador = 0
          vida = 10 + valor_amarzenado[3]
          mp = 10 + valor_amarzenado[17]

          while (controle3 > 1):
              somador = valor_amarzenado[3] + random.randint(1,valor_amarzenado[19])

              if (somador > 0):
                 vida = vida + somador
              
              controle3 = controle3 - 1
            
          controle3 = lvl

          while (controle3 > 1):
              somador =  valor_amarzenado[17] + random.randint(1,valor_amarzenado[20])

              if (somador > 0):
                 mp = mp + somador
              
              controle3 = controle3 - 1 

          #comparador de ativação de conjuntos de iteins

          if (x.values['conjunto1'] == True):

                  pagina2["B2"].value = "Saco de dormir x1"
                  pagina2["C2"].value = "Corda x1"
                  pagina2["D2"].value = "Kit de escalada x1" 

                  pagina2["B3"].value = "Frasco x2"
                  pagina2["C3"].value = "Lâmpada x1"
                  pagina2["D3"].value = "Mochila media 10 st" 

                  


          # diretorios dos valores da plhanilha "Parte da frente" que irão receber os valores

          pagina1["B1"].value = lvl #lvl
          pagina1["D1"].value = vida #vida
          pagina1["F1"].value = mp #mp
          pagina1["H1"].value = '100' #dinheiro
          pagina1["H3"].value = nome #nome

          #bruto
          pagina1["B4"].value = valor_amarzenado[0] #STR
          pagina1["B5"].value = valor_amarzenado[2] #CON
          pagina1["B6"].value = valor_amarzenado[4] #AC
          pagina1["B7"].value = valor_amarzenado[6] #AG
          pagina1["B8"].value = valor_amarzenado[8] #INT
          pagina1["B9"].value = valor_amarzenado[10] #SAB
          pagina1["B10"].value = valor_amarzenado[12] #CHA
          pagina1["B11"].value = valor_amarzenado[14] #ST
          pagina1["B12"].value = valor_amarzenado[16] #MA/
          pagina1["B14"].value = valor_amarzenado[18] #MUV

          #real
          pagina1["C4"].value = valor_amarzenado[1] #STR 2
          pagina1["C5"].value = valor_amarzenado[3] #CON 2
          pagina1["C6"].value = valor_amarzenado[5] #AC 2
          pagina1["C7"].value = valor_amarzenado[7] #AG 2
          pagina1["C8"].value = valor_amarzenado[9] #INT 2
          pagina1["C9"].value = valor_amarzenado[11] #SAB 2
          pagina1["C10"].value = valor_amarzenado[13] #CHA 2
          pagina1["C11"].value = valor_amarzenado[15] #ST 2
          pagina1["C12"].value = valor_amarzenado[17] #MA/ 2
          


          pagina1["E4"].value = '' #CABEÇA NOME
          pagina1["F4"].value = '' #CABEÇA CA
          pagina1["E10"].value = 10 + valor_amarzenado[3] #CA
          pagina1["E11"].value = 10 + valor_amarzenado[11] #CM


          pagina1["E13"].value = '1' #PERSUADIR 
          pagina1["E14"].value = '1' #ARQUEOLOGIA 
          pagina1["E15"].value = '1' #HISTORIA 
          pagina1["E16"].value = '1' #MEDICINA 
          pagina1["E17"].value = '1' #OCULTISMO 
          pagina1["E18"].value = '1' #FURTIVIDADE 
          pagina1["E19"].value = '1' #LOCALIZAR 
          pagina1["E20"].value = '1' #INTIMIDAÇÃO 
          pagina1["E21"].value = '1' #ESCALAR 
          pagina1["E22"].value = '1' #ESCULTAR 


          pagina1["H13"].value = '1' #ENCONTRAR 
          pagina1["H14"].value = '1' #OLCULTAR 
          pagina1["H15"].value = '1' #CAVALGAR 
          pagina1["H16"].value = '1' #ATUAÇÃO 
          pagina1["H17"].value = '1' #ATLETISMO 
          pagina1["H18"].value = '1' #ACROBACIA 
          pagina1["H19"].value = '1' #INTUIÇÃO 
          pagina1["H20"].value = '1' #PERCEPLÇÃO 
          pagina1["H21"].value = '1' #PRESTIGITAÇÃO 
          pagina1["H22"].value = '1' #RASTREIO 

          pagina1["A16"].value = p_estatus    #Pontos de status 
          pagina1["B16"].value = p_habilidade #Pontos de habilidade



          book.save('Parte da frente.xlsx')
