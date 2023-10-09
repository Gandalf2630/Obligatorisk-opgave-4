from socket import *


servername = 'localhost'
serverport = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((servername,serverport))

sentence = input('Indtast linje: ')
data = sentence.encode()
clientSocket.send(data)


datatilbage = clientSocket.recv(2048)
sentenceTilbage = datatilbage.decode()

print ('Modtaget tekst ', sentenceTilbage)
clientSocket.close()