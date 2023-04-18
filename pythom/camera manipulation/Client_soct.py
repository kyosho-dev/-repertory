#===========cliente.py========================
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

envia = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#socket.socket()
envia.connect(("127.0.0.1",55555))# IP e a porta usada no servidor
arquivo = open ("oi.txt", "rb")# nome do arqquivo
ler_buffer = arquivo.read(1024) #começa a ler o arquivo e armazenar em um buffer

while (ler_buffer):
    envia.send(ler_buffer) #envia o condeudo do buffer para o servidor
    ler_buffer = arquivo.read(1024)# armazena mais conteudo do arquivo no buffer
envia.close()