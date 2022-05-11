from socket import *
import uuid
import datetime

#Create clock object
aCloc = datetime.datetime.now()
def timeCheck(intime):
	a60sec = datetime.timedelta(seconds=60)
	if (aCloc.strftime("%X") > (intime)): #+ a60sec)):
		validTime = False
	else:
		validTime = True	
	return validTime
	
def ackMenu():

        print("client:Choose which option you want to proceed")
        print("1. Release:")
        print("2. Renew:")
        print("3. quit:")
        menuChoice = input("Enter 1, 2, or 3\n")
 
        return menuChoice


serverName = 'localhost'
serverPort = 20002
aMacAdr = "C146E7MA24C6"
clientSocket = socket(AF_INET, SOCK_DGRAM)

#store computers macaddr in mac
mac = (hex(uuid.getnode()))

#print(mac)
#mac = mac[2:]
#print(mac)
dmessage = "0:" + aMacAdr#mac#input('Input lowercase sentence:')


clientSocket.sendto(dmessage.encode().lower(),(serverName, serverPort))


#clientSocket.sendto(message.encode().lower(),(serverName, serverPort))
#modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
#print (modifiedMessage.decode())
while 1:

    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print (modifiedMessage.decode())
    ourMes=modifiedMessage.decode()

    if(ourMes[0] == '1'):
        #print(ourMes[2:14])
        print("client:Offer recieved")
        if(ourMes[2:14] == aMacAdr.lower()):
            print("client:Mac Addresses Match")
            print(ourMes[-8:])
            t=ourMes[-8:]
            if(timeCheck(t) == True):
                print("client:Sending Request")
                sendReq = "2:" + ourMes[2:]
                print(sendReq)
                clientSocket.sendto(sendReq.encode().lower(),(serverName,serverPort))

        else:#close socket if incorrect mac recieved
            print("client:Error incorrect MAC address")
            clientSocket.close()

    elif(ourMes[0] == '3'):
        print("client:Acknowledgement Recieved")
        print(ourMes[2:])
        if(ourMes[2:14] != aMacAdr.lower()):
            print("client:Mac address resolution error")
            clientSocket.close()

        else:
            print("client:The IP address " + ourMes[15:-8] + " was assigned to this client, which will expire at time " + ourMes[-8:] )

            menuPic = 0
            while(menuPic != "3"):#"1" and menuPic!= "2" and menuPic != "3" ):
                menuPic = ackMenu()            
    
                if(menuPic == "1"):
                #send release message to server contain macaddr && ipaddr
                    print("client:Sending Release Message")
                    release = "4:" + ourMes[2:-8]
                    print(release)
                    clientSocket.sendto(release.encode().lower(),(serverName, serverPort))
                    
                elif(menuPic == "2"):
                #send renew message to server contain macaddr && ipaddr
                    print("client:Sending Renew Message")
                    renew = "5:" + ourMes[2:-8]
                    print(renew)
                    clientSocket.sendto(renew.encode().lower(),(serverName, serverPort))
                    
                elif(menuPic == "3"):
                    clientSocket.close()
                    
            #else:
            #    print("Invalid entry please choose one of these 3 options")
#                menuPic = ackMenu()
                    
                    
    #if a decline message is sent
    elif(ourMes[0] == '7'):
        print("client:Declined")
        print(ourMes[2:])
        clientSocket.close()
        
    elif(ourMes[0] == '9'):
        print(ourMes[2:])
        clientSocket.close()

'''
newmodMessage, serverAddress = clientSocket.recvfrom(2048)
print(newmodMessage.decode())
anAck = newmodMessage.decode()
if(anAck[0] == '3'):
    if(anAck[2:14] == aMacAdr.lower()):
        repon = "The IP address " + anAck[15:-8] + "was assigned to this client"
    else:
        print("Error incorrect MAC address")
        clientSocket.close()
'''

#1:b146e7ca24d8 198.168.45.1 Sun 
#client

clientSocket.close()
