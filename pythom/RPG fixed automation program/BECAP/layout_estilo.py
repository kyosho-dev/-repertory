import PySimpleGUI as sg

#cria o layout da pagina

Pagina_1 = [
    
    #NOME E NIVEL 
    
    [sg.Text('Nome' , size=(5,0)), sg.Input(key="nome", size=(20,0)), sg.Text('Nivel' , size=(3,0)), sg.Input(key="Nivel" , size=(3,0))],
    

    #CLASSES
    [sg.Radio('Mago','cartoes',key ="Mago"), sg.Radio('Mago da sorte','cartoes',key="Mago da sorte"), sg.Radio('Elementarista','cartoes',key="Elementarista"), sg.Radio('Engenheiro','cartoes',key="Engenheiro"), sg.Radio('Alchemist','cartoes',key="Alchemist"),sg.Radio('Domador','cartoes',key="Domador")],
    [sg.Text('')],
    [sg.Radio('Arkanoid','cartoes',key ="Arkanoid"), sg.Radio('Mestre das almas','cartoes',key="Mestre das almas"), sg.Radio('Suporte','cartoes',key="Suporte"), sg.Radio('Guerreiro','cartoes',key="Guerreiro"), sg.Radio('Escudeiro','cartoes',key="Escudeiro"),sg.Radio('Brute force warrior','cartoes',key="Brute force warrior")],
    [sg.Text('')],
    [sg.Radio('Barbaro','cartoes',key ="Barbaro"), sg.Radio('Guerreiro 2 SW','cartoes',key="Guerreiro 2 SW"), sg.Radio('Guerreiro 2H','cartoes',key="Guerreiro 2H"), sg.Radio('Ceifador','cartoes',key="Ceifador"), sg.Radio('Monje','cartoes',key="Monje"), sg.Radio('Arqueiro','cartoes',key="Arqueiro"),sg.Radio('Cruzader','cartoes',key="Cruzader")],
    [sg.Text('')],
    [sg.Radio('Necromance','cartoes',key ="Necromance"), sg.Radio('Clerigo','cartoes',key="Clerigo"), sg.Radio('Bardo','cartoes',key="Bardo"), sg.Radio('Orador','cartoes',key="Orador"), sg.Radio('Mediun','cartoes',key="Mediun"),sg.Radio('Druida','cartoes',key="Druida")],
    [sg.Text('')],
    [sg.Radio('Samurai','cartoes',key ="Samurai"), sg.Radio('Ninja','cartoes',key="Ninja"), sg.Radio('Ceifeiro','cartoes',key="Ceifeiro"), sg.Radio('Ladino','cartoes',key="Ladino")],
    [sg.Text('')],
    [sg.Text('Lista de conjuntos')],
    [sg.Text('')],
    [sg.Radio('Conjunto do aventureiro','conjutos',key ="conjunto1")],
    [sg.Radio('Conjunto do pesquisador','conjutos',key ="conjunto2")],
    [sg.Radio('Conjunto do ladrão','conjutos',key ="conjunto3")],
    [sg.Radio('Conjunto do alquimista','conjutos',key ="conjunto4")],
    [sg.Radio('Conjunto do ferreiro','conjutos',key ="conjunto5")],
    [sg.Text('')],
    [sg.Button('Enviar')] 
]