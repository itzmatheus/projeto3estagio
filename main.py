"""
Principal
Versão: 0.1
Criado por: Matheus José
matheusjoselfm@gmail.com
Data: 11/2017
"""
from func import *

arq = open('files/convidados.txt','r') #Informe o diretório da lista.
lista = import_invites(arq)
arq.close()

create_pdf(lista)

attachment = open('files/convidados.pdf','rb')
send_mail(attachment)
attachment.close()
