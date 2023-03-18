from socket import *

serverPort = 11500
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is listening")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    ClientSendMessage1 = str(message.decode())
    print(ClientSendMessage1 + " and length of the string is ",end="")
    print((len(ClientSendMessage1)))
    ClientSendMessage1 = str(message.decode()).upper() + " and length of this message is " +str(len(ClientSendMessage1))
    serverSocket.sendto(ClientSendMessage1.encode(), clientAddress)
