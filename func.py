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

#Script p receber lista de convidados e adicionar os valores num dicionario
def import_invites(arq):  #Função que importa um arquivo de texto e adiciona os valores num dicionario.
        colecao = {}
        arq_lines = arq.readlines() #Lendo todas as linhas do arquivo e colocando numa lista.
        for linha in arq_lines[1:]: #Todas as linhas seram lidas e cortadas onde tem espaço.
            lista = linha.split()
            for linha_2 in lista: #Segundo corte agora para separar nome(chave) e o telefone(valor) e adicionar num dicionario.
                nome,telefone = linha_2.split('-')
                colecao[nome] = telefone
        return colecao

#Script p criar pdf
def create_pdf(lista)
    try:
        nome_pdf = 'convidados'
        pdf = canvas.Canvas('files/{}.pdf'.format(nome_pdf))
        y = 300
        for nome,telefone in lista.items():
            y += 20
            pdf.drawString(247,y, '{} : {}'.format(nome,telefone))
        pdf.setFont("Helvetica-Oblique", 14)
        pdf.drawString(205,750, '===/ Lista de Convidados \===')
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(245,724, 'Nomes e Telefones')
        pdf.save()
        print('PDF Criado com sucesso!\nLocal:/files/{}.pdf'.format(nome_pdf))
    except:
        print('Erro ao gerar o pdf /files/{}.pdf'.format(nome_pdf))

#Script p enviar e-mail com arquivo indexado
#Criado por http://naelshiab.com/tutorial-send-email-python/
def send_mail(attachment):
    try:
        fromaddr = "Email para enviar"
        toaddr = "Email p receber"

        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Lista de convidados - Equipe: Matheus e Gabriel"

        body = "\nSegue a lista de convidados em PDF. \nAtt, Matheus José e Gabriel Santana."

        msg.attach(MIMEText(body, 'plain'))

        filename = "convidados.pdf"
        # attachment = open("files/convidados.pdf", "rb")

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        msg.attach(part)

        server = smtplib.SMTP('smtp.outlook.com', 587)
        server.starttls()
        server.login(fromaddr, "SenhaAquiDoEMail")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        print('Email enviado para {}\nTítulo: {}'.format(msg['To'],msg['Subject']))
    except:
        print("Ocorreu um erro no processo de envio do e-mail para {}.\n Por favor, tente novamente!".format(msg['To']))
