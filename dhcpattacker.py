from socket import *
import datetime


#Create clock object
aCloc = datetime.datetime.now()


serverName = 'localhost'
serverPort = 20002
randMacPre = "B146E7CA24"
clientSocket = socket(AF_INET, SOCK_DGRAM)

#while 1:
#    for x in range(10,26):
        #Sending discovery message to the server
#        ddosMessage = "0:" + randMacPre + str(x) #+ aMacAdr#mac#input('Input lowercase sentence:')
#        clientSocket.sendto(ddosMessage.encode().lower(),(serverName, serverPort))
x = 10
while (x < 24):
        ddosMessage = "0:" + randMacPre + str(x) #+ aMacAdr#mac#input('Input lowercase sentence:')
        clientSocket.sendto(ddosMessage.encode().lower(),(serverName, serverPort))
        x = x + 1


