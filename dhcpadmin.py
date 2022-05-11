from socket import *
import datetime


#Create clock object
aCloc = datetime.datetime.now()


serverName = 'localhost'
serverPort = 20002
#aMacAdr = "B146E7CA24D8"
clientSocket = socket(AF_INET, SOCK_DGRAM)

#Sending lis message to the server
lisMessage = "6:" #+ aMacAdr#mac#input('Input lowercase sentence:')
clientSocket.sendto(lisMessage.encode().lower(),(serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print (modifiedMessage.decode())
lisMesStr=modifiedMessage.decode()
#outputLis = lisMesStr.split()
#print(outputLis)

