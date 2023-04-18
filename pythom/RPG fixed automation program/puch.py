from cgitb import text
from itertools import count
from turtle import st

import openpyxl

#abre o documento para pegar  os dados 
lista_de_clases = openpyxl.load_workbook('lista de classes.xlsx')

pagina_classes = lista_de_clases['Página1']


        




#VALORES DAS CLASSES  

#(STR 0 1) (CON 2 3) (AC 4 5) (AG 6 7) (INT  8 9) (SAB 10 11) (CHA 12 13) (ST 14 15) (MA/ 16 17) (MUV 18) (VIT 19) (MP 20) 

#                         STR     CON     AC      AG      INT    SAB     CHA    ST      MA/    MUV   DVIDA    DMANA 
Mago_V =                [ 0,0,    0,0,    0,0,   0,0,     0,0,   0,0,    0,0,   0,0,    0,0,    0,     4,       10    ]
Mago_da_sorte_V =       [ 0,0,    0,0,    0,0,   0,0,     0,0,   0,0,    0,0,   0,0,    0,0,    0,     4,       10    ]
Elementarista_V =       [ 0,0,    0,0,    0,0,   0,0,     0,0,   0,0,    0,0,   0,0,    0,0,    0,     4,       10    ]
Engenheiro_V =          [ 0,0,    0,0,    0,0,   0,0,     0,0,   0,0,    0,0,   0,0,    0,0,    0,     4,       10    ]
Alchemist_V =           [ 0,0,    0,0,    0,0,   0,0,     0,0,   0,0,    0,0,   0,0,    0,0,    0,     4,       10    ]
Domador_V =             [ 0,0,    0,0,    0,0,   0,0,     0,0,   0,0,    0,0,   0,0,    0,0,    0,     4,       10    ]
Arkanoid_V =            [ 0,0,    0,0,    0,0,   0,0,     0,0,   0,0,    0,0,   0,0,    0,0,    0,     4,       10    ]
Mestre_das_almas_V =    [ 0,0,    0,0,    0,0,   0,0,     0,0,   0,0,    0,0,   0,0,    0,0,    0,     4,       10    ]
Suporte_V =             [ 0,0,    0,0,    0,0,   0,0,     0,0,   0,0,    0,0,   0,0,    0,0,    0,     4,       10    ]


Guerreiro_V =           [ 0,0,    0,0,    0,0,   0,0,     0,0,   0,0,    0,0,   0,0,    0,0,    0,     4,       10    ]
Escudeiro_V =           [ 0,0,    0,0,    0,0,   0,0,     0,0,   0,0,    0,0,   0,0,    0,0,    0,     4,       10    ]
Brute_force_warrior_V = [ 0,0,    0,0,    0,0,   0,0,     0,0,   0,0,    0,0,   0,0,    0,0,    0,     4,       10    ]
Barbaro_V =             [ 0,0,    0,0,    0,0,   0,0,     0,0,   0,0,    0,0,   0,0,    0,0,    0,     4,       10    ]
Guerreiro_2_SW_V =      [ 0,0,    0,0,    0,0,   0,0,     0,0,   0,0,    0,0,   0,0,    0,0,    0,     4,       10    ]
Guerreiro_2H_V =        [ 0,0,    0,0,    0,0,   0,0,     0,0,   0,0,    0,0,   0,0,    0,0,    0,     4,       10    ]
Ceifador_V =            [ 0,0,    0,0,    0,0,   0,0,     0,0,   0,0,    0,0,   0,0,    0,0,    0,     4,       10    ]
Monje_V =               [ 0,0,    0,0,    0,0,   0,0,     0,0,   0,0,    0,0,   0,0,    0,0,    0,     4,       10    ]


Arqueiro_V =            [ 0,0,    0,0,    0,0,   0,0,     0,0,   0,0,    0,0,   0,0,    0,0,    0,     4,       10    ]
Cruzader_V =            [ 0,0,    0,0,    0,0,   0,0,     0,0,   0,0,    0,0,   0,0,    0,0,    0,     4,       10    ]

Necromance_V =          [ 0,0,    0,0,    0,0,   0,0,     0,0,   0,0,    0,0,   0,0,    0,0,    0,     4,       10    ]
Clerigo_V =             [ 0,0,    0,0,    0,0,   0,0,     0,0,   0,0,    0,0,   0,0,    0,0,    0,     4,       10    ]
Bardo_V =               [ 0,0,    0,0,    0,0,   0,0,     0,0,   0,0,    0,0,   0,0,    0,0,    0,     4,       10    ]
Orador_V =              [ 0,0,    0,0,    0,0,   0,0,     0,0,   0,0,    0,0,   0,0,    0,0,    0,     4,       10    ]
Mediun_V =              [ 0,0,    0,0,    0,0,   0,0,     0,0,   0,0,    0,0,   0,0,    0,0,    0,     4,       10    ]
Druida_V =              [ 0,0,    0,0,    0,0,   0,0,     0,0,   0,0,    0,0,   0,0,    0,0,    0,     4,       10    ]


Samurai_V =             [ 0,0,    0,0,    0,0,   0,0,     0,0,   0,0,    0,0,   0,0,    0,0,    0,     4,       10    ]
Ninja_V =               [ 0,0,    0,0,    0,0,   0,0,     0,0,   0,0,    0,0,   0,0,    0,0,    0,     4,       10    ]
Ceifeiro_V =            [ 0,0,    0,0,    0,0,   0,0,     0,0,   0,0,    0,0,   0,0,    0,0,    0,     4,       10    ]
Ladino_V =              [ 0,0,    0,0,    0,0,   0,0,     0,0,   0,0,    0,0,   0,0,    0,0,    0,     4,       10    ]





def puchar_estatos():

  for i in range(0, 18, 2): #valores brutos
        
        if(i == 0):
            t1 = "B"
            

        if(i == 2):
            t1 = "C"
            
            
        if(i == 4):
            t1 = "D"
            

        if(i == 6):
            t1 = "E"
            
            
        if(i == 8):
            t1 = "F"
            

        if(i == 10):
            t1 = "G"
            
            
        if(i == 12):
            t1 = "H"
            

        if(i == 14):
            t1 = "I"
            
            
        if(i == 16):
            t1 = "J"
            


        Mago_V[i] =                int(pagina_classes[(t1 + "2")].value)
        Mago_da_sorte_V[i] =       int(pagina_classes[(t1 + "5")].value)
        Elementarista_V[i] =       int(pagina_classes[(t1 + "8")].value)
        Engenheiro_V[i] =          int(pagina_classes[(t1 + "11")].value)
        Alchemist_V[i] =           int(pagina_classes[(t1 + "14")].value)
        Domador_V[i] =             int(pagina_classes[(t1 + "17")].value)
        Arkanoid_V[i] =            int(pagina_classes[(t1 + "20")].value)
        Mestre_das_almas_V[i] =    int(pagina_classes[(t1 + "23")].value)
        Suporte_V[i] =             int(pagina_classes[(t1 + "26")].value)



        Guerreiro_V[i] =           int(pagina_classes[(t1 + "29")].value)
        Escudeiro_V[i] =           int(pagina_classes[(t1 + "32")].value)
        Brute_force_warrior_V[i] = int(pagina_classes[(t1 + "35")].value)
        Barbaro_V[i] =             int(pagina_classes[(t1 + "38")].value)
        Guerreiro_2_SW_V[i] =      int(pagina_classes[(t1 + "41")].value)
        Guerreiro_2H_V[i] =        int(pagina_classes[(t1 + "44")].value)
        Ceifador_V[i] =            int(pagina_classes[(t1 + "47")].value)
        Monje_V[i] =               int(pagina_classes[(t1 + "50")].value)

        Arqueiro_V[i] =            int(pagina_classes[(t1 + "53")].value)
        Cruzader_V[i] =            int(pagina_classes[(t1 + "56")].value)

        Necromance_V[i] =          int(pagina_classes[(t1 + "59")].value)
        Clerigo_V[i] =             int(pagina_classes[(t1 + "62")].value)
        Bardo_V[i] =               int(pagina_classes[(t1 + "65")].value)
        Orador_V[i] =              int(pagina_classes[(t1 + "68")].value)
        Mediun_V[i] =              int(pagina_classes[(t1 + "71")].value)
        Druida_V[i] =              int(pagina_classes[(t1 + "74")].value)


        Samurai_V[i] =             int(pagina_classes[(t1 + "77")].value)
        Ninja_V[i] =               int(pagina_classes[(t1 + "80")].value)
        Ceifeiro_V[i] =            int(pagina_classes[(t1 + "83")].value)
        Ladino_V[i] =              int(pagina_classes[(t1 + "86")].value)
        



  for i in range(1, 18, 2): #valores reais
        
    if(i == 1):
        t1 = "B"
        

    if(i == 3):
        t1 = "C"
        
        
    if(i == 5):
        t1 = "D"
        

    if(i == 7):
        t1 = "E"
        
        
    if(i == 9):
        t1 = "F"
        

    if(i == 11):
        t1 = "G"
        
        
    if(i == 13):
        t1 = "H"
        

    if(i == 15):
        t1 = "I"
        
        
    if(i == 17):
        t1 = "J"
        


    Mago_V[i] =                int(pagina_classes[(t1 + "3")].value)
    Mago_da_sorte_V[i] =       int(pagina_classes[(t1 + "6")].value)
    Elementarista_V[i] =       int(pagina_classes[(t1 + "9")].value)
    Engenheiro_V[i] =          int(pagina_classes[(t1 + "12")].value)
    Alchemist_V[i] =           int(pagina_classes[(t1 + "15")].value)
    Domador_V[i] =             int(pagina_classes[(t1 + "18")].value)
    Arkanoid_V[i] =            int(pagina_classes[(t1 + "21")].value)
    Mestre_das_almas_V[i] =    int(pagina_classes[(t1 + "24")].value)
    Suporte_V[i] =             int(pagina_classes[(t1 + "27")].value)



    Guerreiro_V[i] =           int(pagina_classes[(t1 + "30")].value)
    Escudeiro_V[i] =           int(pagina_classes[(t1 + "33")].value)
    Brute_force_warrior_V[i] = int(pagina_classes[(t1 + "36")].value)
    Barbaro_V[i] =             int(pagina_classes[(t1 + "39")].value)
    Guerreiro_2_SW_V[i] =      int(pagina_classes[(t1 + "42")].value)
    Guerreiro_2H_V[i] =        int(pagina_classes[(t1 + "45")].value)
    Ceifador_V[i] =            int(pagina_classes[(t1 + "48")].value)
    Monje_V[i] =               int(pagina_classes[(t1 + "51")].value)

    Arqueiro_V[i] =            int(pagina_classes[(t1 + "54")].value)
    Cruzader_V[i] =            int(pagina_classes[(t1 + "57")].value)

    Necromance_V[i] =          int(pagina_classes[(t1 + "60")].value)
    Clerigo_V[i] =             int(pagina_classes[(t1 + "63")].value)
    Bardo_V[i] =               int(pagina_classes[(t1 + "66")].value)
    Orador_V[i] =              int(pagina_classes[(t1 + "69")].value)
    Mediun_V[i] =              int(pagina_classes[(t1 + "72")].value)
    Druida_V[i] =              int(pagina_classes[(t1 + "75")].value)


    Samurai_V[i] =             int(pagina_classes[(t1 + "78")].value)
    Ninja_V[i] =               int(pagina_classes[(t1 + "81")].value)
    Ceifeiro_V[i] =            int(pagina_classes[(t1 + "84")].value)
    Ladino_V[i] =              int(pagina_classes[(t1 + "87")].value)

