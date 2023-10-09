from socket import *
from threading import *
import random

serverPort = 12000

def handleClient(clientSocket, addr):
    sentence = clientSocket.recv(2048).decode()


    splitterText = sentence.split()
    Text = ''
    if (splitterText[0].lower() == 'add'): 
        talx = int(splitterText[1])
        taly = int(splitterText[2])
        Text = f'{talx}+{taly}= {(talx+taly)}'
    elif (splitterText[0].lower() == 'substract'): 
        talx = int(splitterText[1])
        taly = int(splitterText[2])
        Text = f'{talx}-{taly}= {(talx-taly)}'
    elif (splitterText[0].lower() == 'add'): 
        talx = int(splitterText[1])
        taly = int(splitterText[2])
        Text = f'{random.randint(talx, taly)}'
    else:
        Text = f'ikke gyldig i metoden {splitterText[0]}'

        clientSocket.send(Text.encode())

        clientSocket.close()

        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.bind(('', serverPort))
        serverSocket.listen(1)
        print('The server is up and running', serverPort)

        while True:
            connectionsSocket, addr = serverSocket.accept()
            print('Forrbundet til en mysh fra en anden adresse', addr)
            Thread(target=handleClient, args=(connectionsSocket,addr)).start()