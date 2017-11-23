#coding: utf-8
"""
Principal
Versão: 0.1
Criado por: Matheus José
matheusjoselfm@gmail.com
Data: 11/2017
"""
from func import *

arq = open('files/convidados.txt','r') #leitura do arquivo de texto
lista = import_invites(arq)# variavel lista armazena o valor retornado pela funçao.
arq.close()#fechando arquivo

pdf = create_pdf(lista)#Chamando a função para criar pdf, com parâmentro lista.

attachment = open('files/{}.pdf'.format(pdf),'rb')# para leitura do arquivo pdf
send_mail(attachment)#chamando a função que envia e-mail
attachment.close()# fechando arquivo.
