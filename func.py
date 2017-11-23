#coding: utf-8
"""
Funções
Versão: 0.1
Criado por: Matheus José
matheusjoselfm@gmail.com
Data: 11/2017
"""
from reportlab.pdfgen import canvas
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#Parte 1 do projeto
#Script p receber arquivo com a lista de convidados e adicionar os valores em um  dicionario
def import_invites(arq):#Função para importa arquivo de texto e adicionar em um dicionario.
        colecao = {}                 #Criando dicionario, para guardar nome como chave e telefone como valor.
        arq_lines = arq.readlines() #Lendo todas as linhas do arquivo e colocando numa lista.
        for linha in arq_lines[1:]: #Todas as linhas seram lidas e cortadas onde tem espaço.
            lista = linha.split()
            for linha_2 in lista: #Segundo corte agora para separar o hífen e guardar nome(chave) e o telefone(valor) no dicionario.
                nome,telefone = linha_2.split('-')
                colecao[nome] = telefone
        return colecao #rotornando dicionario
#Parte 2 do projeto
#Script p criar pdf
def create_pdf(lista):
    try: #Método para testar o funcionamento a baixo com mensagem de sucesso ou erro
        global nome_pdf  #nome do pdf vai ser uma variavel global
        nome_pdf = input('Informe o nome do PDF: ') #vai receber nome do arquivo pdf
        pdf = canvas.Canvas('files/{}.pdf'.format(nome_pdf))#Linha para gerar arquivo pdf
        x = 300
        for nome,telefone in lista.items():# laço de repetição para escrever nome e telefone da lista no pdf
            x += 20 # As linhas serão escritas no pdf a partir do eixo x na posição 300 e vai subindo de 20 em 20
            pdf.drawString(247,x, '{} : {}'.format(nome,telefone))
        pdf.setFont("Helvetica-Oblique", 14)#Escolhendo fonte para título
        pdf.drawString(205,750, '===/ Lista de Convidados \===')
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(245,724, 'Nomes e Telefones')
        pdf.save()
        print('\nPDF Criado com sucesso!\nLocal:/files/{}.pdf'.format(nome_pdf)) #Se a execução for realizada com sucessco, vai apresentar essa mensagem.
    except: #Tratamento com mensagem de erro caso não seja possível gerar o pdf
        print('\nErro ao gerar o pdf /files/{}.pdf'.format(nome_pdf))# Se apresentar erro na exeucação, vai apresntar essa mensagem.
    return nome_pdf
#Parte 3 do projeto
#Script p enviar e-mail com arquivo indexado
#Criado por http://naelshiab.com/tutorial-send-email-python/
def send_mail(attachment):
    try: #Método para tratamento de erros
        fromaddr = "projeto3estagio@outlook.com" # E-mail que vai ser utilizado para encaminhar arquivo pdf.
        toaddr = 'matheusjoselfm@gmail.com'#E-mail que vai receber arquivo pdf.
        msg = MIMEMultipart()#váriavel que vai receber função multipar

        msg['From'] = fromaddr #Adicionar no dicionario o e-mail remetente
        msg['To'] = toaddr #Adicionar no dicionario o e-mail destinatário
        msg['Subject'] = "Contatos - Equipe: Matheus e Gabriel" # Assunto do e-mail

        body = "\nSegue os contatos em anexo." # Corpo do e-mail

        msg.attach(MIMEText(body, 'plain'))

        filename = nome_pdf # nome do arquivo pdf

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s.pdf" % filename)#Vai criar titulo do pdf no corpo do e-mail

        msg.attach(part)

        server = smtplib.SMTP('smtp.outlook.com', 587)# Configurar servidor smtp
        server.starttls()
        server.login(fromaddr, "projeto123456")#Recebendo e-mail do remetende com a senha
        text = msg.as_string()#ajustando mensagem com a função string
        server.sendmail(fromaddr, toaddr, text)# E-mal do remetente, distinatário e o texto.
        server.quit()
        print('\nEmail enviado para {}\nTítulo: {}'.format(msg['To'],msg['Subject'])) # se e-mail for enviado, vai apresentar essa mensagem
    except:
        print("\nOcorreu um erro no processo de envio do e-mail para {}.\n Por favor, tente novamente!".format(msg['To']))# se e-mail não for enviado, vai apresentar essa mensagem.
