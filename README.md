# Projeto de Algoritmos e Programação - 3º Estágio
#### Equipe: Matheus José e Gabriel Santana

Sobre o projeto: Criação de uma aplicação para importar um arquivo de texto, gerar um PDF com as informações coletadas e enviar por e-mail.

##### Requisito necessário para funcionamento da aplicação: Python 3
Python 3 -> https://www.python.org/downloads/

Para verificar se o python está instalado digite no terminal:
```sh
~/projeto3estagio $ python --version
Python 3.6.3
```
#### OBS: Para rodar a aplicação, sugiro criar um ambiente isolado para desenvolvimento e instalação de algumas bibliotecas externas utilizadas no projeto!

#### 1 - Passo: Ambiente isolado de desenvolvimento
Virtualenv - https://virtualenv.pypa.io/en/stable/installation/
- De inicio precisamos criar o ambiente isolado. Ele serve basicamente para gerenciar-mos versões de uma aplicação, gerando maior controle de dependências usadas, por exemplo. 

Digite no terminal:
```sh
~/projeto3estagio $ python3 -m venv NomeDoAmbiente
```
- Verifique se uma pasta foi criada com o nome do ambiente que você escolheu.
- Caso a pasta com o nome escolhido for criada, agora é hora de ativar.

Caso use Linux digite no terminal:
```sh
~/projeto3estagio $ source NomeDoAmbiente/bin/activate
```
Caso use Windows digite no terminal:
```sh
~/projeto3estagio $ NomeDoAmbiente\Scripts\activate
```
- Veja se ficou parecido com a linha abaixo:
```sh
(NomeDoAmbiente)   ~/projeto3estagio $
```
- Se apareceu o nome do ambiente antes da linha de código, então o ambiente está ativado.
#### 2 - Passo: Instalação de bibliotecas externas
- Para instalação de bibliotecas externas é necessário um gerenciador de pacotes, no caso do python é o PIP.
- OBS: Normalmente o pip é instalado quando criamos um ambiente virtual. Caso não venha instalado no seu ambiente baixe-o e realize a instalação. É bem fácil! 

- PIP -> https://pypi.python.org/pypi/pip#downloads

Com o ambiente ativado digite:
 ```sh
(NomeDoAmbiente)  ~/projeto3estagio $ pip --version
pip 9.0.1 from...
```
- Com o pip instalado, vamos instalar algumas bibliotecas externas que utilizei para criação da aplicação. Como exemplo o reportlab, uma ferramenta que facilita gerar PDF.
- OBS: Certifique-se de está na mesma pasta que o arquivo 'requirements.txt', pois nele está todas as bibliotecas utilizadas.

Para instalar todas as bibliotecas digite:
 ```sh
(NomeDoAmbiente)  ~/projeto3estagio $ pip install -r requirements.txt
```
- Se não aparecer nenhum erro, houve sucesso nas instalações e podemos prosseguir para o último passo.
#### 3 - Passo: Rodar a aplicação
- No projeto existem os 2 arquivos principais em python, o 'func.py' está contigo as importações de bibliotecas e as funções criadas e o 'main.py' o arquivo executável da aplicação.

Para rodar-la basta digitar no terminal:
 ```sh
(NomeDoAmbiente)  ~/projeto3estagio $ python main.py
```
#### Detalhes da aplicação
- func.py -> Arquivo com as funções criadas p/ o projeto.
- main.py -> Arquivo executável do projeto, onde invoca as funções.
- requirements.txt -> arquivo criado com os nomes das bibliotecas instaladas no ambiente virtual para uso da aplicação.
- files -> Pasta para armazenar os documentos.
- files/convidados.txt -> Arquivo de texto contendo lista de convidados.
- files/convidados.pdf -> PDF Gerado pela aplicação.
- files/Projeto Algoritmos e Programação.pdf -> PDF contendo informações para o projeto. 
