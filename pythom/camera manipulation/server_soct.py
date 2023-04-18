#=========servidor.py========================
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
recebe = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#socket.socket()
recebe.bind(("127.0.0.1",55555))#ip que vai ouvir e a porta
recebe.listen(10) # numero de conexões não aceitas, antes de recusar novas

while True:
    sc, address = recebe.accept()

    
    arquivof = open("recebido_oi.txt",'wb') #abrir o arquivo para escrita
    fim =0
    while (fim==0):       
    
        ler_bfferl = sc.recv(1024) #aloca no buffer o que foi recebido
        
        while (ler_bfferl):
                
                arquivof.write(ler_bfferl)# escreve no arquivo o buffer recebido
                ler_bfferl = sc.recv(1024) # aloca o resto no buffer
                
                fim=1
                 
    arquivof.close()


    sc.close()

recebe.close()