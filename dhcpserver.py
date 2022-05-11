from socket import *
import datetime
import numpy

#Create clock object
aCloc = datetime.datetime.now()

#Prefix for ip addresses
ipPre = "198.168.45."
#Create vector list object

#elemVector = numpy.array(5)

# Create time stamp add to add 60 seconds to the current time
def timeStamp():
	add60secs = datetime.timedelta(seconds=60) 	#create a var of 60 seconds
	stamp = aCloc + add60secs			#add 60 seconds to the current time
		
	return stamp.strftime("%X")			#return time with 60 sec increase

def timeCheck(intime):					#checks current time vs para time
	a60sec = datetime.timedelta(seconds=60)
	
	if (aCloc.strftime("%X") > (intime)): #+ a60sec)):
		validTime = False
	else:
		validTime = True
	
	return validTime			#returns bool status false if expired

def timeStampCheck(myveclis):			#checks the validity of vector timestamps
        for num  in list:
            if(myveclis[num][3] > aCloc.strftime("%X")):
                return num%14
            
                
            elif(myveclis[num][3] < aCloc.strftime("%X")):
                pass
        num = -1
        return num
                
                
def macPull(macAddress):			#passes macAddr as parameter and returns it
	macAdd = macAddress
	return macAdd

def recNum(rec):
	recordNumber = rec
	return recordNumber

def ipGrab(lastD):				#takes number returns ip with last digit para
	ipAdd = lastD
	concatIP = "198.168.45.{}" 
	return (concatIP.format(ipAdd))
	
def ackSwitch(ack):				#Changes ack switch based off input
	if ( ack == True ):
		return ack
	else:
		return False

def poolCheck(poolSize):			#Check to see if the ipAddr pool is full or not
	if (poolSize==14):
		poolFull = True
	else:
		poolFull = False
	
	return poolFull
	
def incPoolSize(inPoolSize):			#increases current value of the pool returns it
	inPoolSize = inPoolSize + 1
	return inPoolSize
	
def decPoolSize(dePoolSize):			#decreases current value of the pool returns it
	dePoolSize = dePoolSize - 1
	return dePoolSize
	
def addofferPre(offstr):			#adds offer prefix 1:
	offerstr = ' '.join(offstr)
	return "1:" + offerstr
	
def addackPre(ackstr):				#adds acknowledge prefix 3:
	acknostr = ' '.join(ackstr)
	return "3:" + acknostr


def vecCon():			#Vector constructor
	vecC = [0,0,0,0,0]
	return vecC
    
def vecMake():
	elem = [recNum(1),macPull(1),ipGrab(4),timeStamp(),ackSwitch(False)]
	return elem

def searchLis(alis, key):
	if key in alis:
		return True
	else:
		return False
		
def macLocate(thislis, mkey):
        for pos in range(0,14):
                if(mkey == thislis[pos][1]):
                        return pos

serverPort = 20002
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ('The server is ready to receive')
print(aCloc)
aStamp = timeStamp()
#elemVector = vecMake()
#print(elemVector)
#print(elemVector[3])
#dc = []

#dc = numpy.empty((14,5))		#init data container
#print(dc) 
#init data container
w, h = 5, 14
dc = [[0 for x in range(w)] for y in range(h)]
#print(dc)
for nx in range(0,14):
	dc[nx][2] = ipGrab(nx+1)
	dc[nx][0] = recNum(nx)
#print(dc)


mypoolSize = 0

while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    #print(message.decode())

    rcvm = (message.decode())
    #print(rcvm)

    if(rcvm[0] == '0'):
        print("server:Discover message received")
        #check db for mac
        clientMac = rcvm[2:14]
        print(clientMac)
        if ((searchLis(dc, clientMac)) == False):
            print("server:Mac not found")
            
            if(poolCheck(mypoolSize)==False): #if ipaddr pool is not full

                mypoolSize = incPoolSize(mypoolSize)
                clientIP = ipGrab(mypoolSize)
                newD = [clientMac, clientIP, timeStamp()]
                

                
                #Storing vector element data
                #dc[mypoolSize-1][0] = mypoolSize -1 #% 14
                dc[mypoolSize-1][1] = newD[0] #clientMac
                dc[mypoolSize-1][2] = newD[1]
                dc[mypoolSize-1][3] = newD[2]
                dc[mypoolSize-1][4] = False
                

                
                print("server:Pool not yet full new data being entered:")
                print(newD)
                offMess = addofferPre(newD)
                print("server:Offer Message Being Sent")
                print(offMess)
                serverSocket.sendto(offMess.encode(), clientAddress)
                
                
            elif(poolCheck(mypoolSize) == True): #if pool is full
                #checks the vector timestamps
                #stamResult = timeStampCheck(dc)
                
                sRes = 0
            
                for mpos in range(0,14):
                    if(aCloc.strftime("%X") > dc[mpos][3]):
                        sRes = mpos
                    else:
                        sRes = -1
                
                #if a record has expired use that ipaddr    
                if (sRes != -1 ):
                    newVecData = [sRes, clientMac, dc[sRes][2], timeStamp()]
                    #dc[sRes][0] = sRes #+ 1
                    dc[sRes][1] = newVecData[1]#clientMac
                    dc[sRes][2] = newVecData[2]
                    dc[sRes][3] = newVecData[3]
                    dc[sRes][4] = False                   
                    
                    
                    '''
                if(stamResult != -1 ):
                    newVecData = [stamResult, clientMac, dc[stamResult][2], timeStamp()]
                    dc[stamResult][0] = stamResult #+ 1
                    dc[stamResult][1] = newVecData[1]#clientMac
                    dc[stamResult][2] = newVecData[2]
                    dc[stamResult][3] = newVecData[3]
                    dc[stamResult][4] = False
                    '''
                    #expired time offer message
                    exptoffmess = addofferPre(newVecData)
                    print(extoffmess)
                    serverSocket.sendto(extoffmess.encode(), clientAddress)
                
                else:
                    #if list occupied fully & no record expired
                    #decline request and send decline message
                    print("server:Pool full declining request and sending DECLINE message")
                    declineMessage = '9:404:server: DDoS Server not found'
                    serverSocket.sendto(declineMessage.encode(), clientAddress)
                
        elif ((searchLis(dc, clientMac)) == True):
            print("server:Mac address in the list")
            
            #find location of macaddress in data container
            macloc = macLocate(dc, clientMac) 
	    #if timestamp is not expired directly send ACK message to client w/ client macaddr, ipaddr already assigned and timestamp   
	    
	    #ind = dc.index(clientMac)
	    
            if ((timeCheck(dc[macloc][3])) == True):	#should switch depending if testing
	        #send ack message ipaddr already assigned & timestamp
                print("server:Send ACK message")
                #ackMessage = [elemVector[1], elemVector[2], elemVector[3]]
                #dc[macloc][3] = timeStamp()
                ackMessage = [dc[macloc][1], dc[macloc][2], dc[macloc][3]]
                #print(ackMessage)

                #add acknowledge prefix to message && turn list into string
                ackpMessage = addackPre(ackMessage)
                print(ackpMessage)
                #send ack message to client
                serverSocket.sendto(ackpMessage.encode(), clientAddress)
                
            #if timestamp is expired use same ipaddr 4 client.
            #Update timestamp in server records 4 macaddr
            #then server sends OFFER message to client, contains macaddr same ipaddr and new timestamp
            else:
                #use same ipaddr 4 client		
                #update timestamp 4 macaddr
                print("server:Old timestamp " + dc[macloc][3])
                dc[macloc][3] = timeStamp()
                print("server:New timestamp acquired " + dc[macloc][3])
                #print(elemVector[3])
                #elemVector[3] = timeStamp()
                #print(elemVector[3])

                #send offer message w/ macaddr same ipaddr & new timestamp
                #offerMessage = [elemVector[1], elemVector[2], elemVector[3]]
                #print(offerMessage)
                offerMessage = [dc[macloc][1], dc[macloc][2], dc[macloc][3]]
                print("server:Sending OFFER message")
                offpMess = addofferPre(offerMessage)
                serverSocket.sendto(offpMess.encode(), clientAddress)
	        
	        
    elif(rcvm[0] == '1'):
        print("server:Offer message received")
        
        
    elif(rcvm[0] == '2'):
        print("server:Request message received")
        clientMac = rcvm[2:14]
        #print(clientMac)
        #print(dc[0][1])
        #print(dc)
        #psearch = searchLis(dc, clientMac)
        #print(psearch)
        macloc = macLocate(dc, clientMac)
        #print(macloc)
        #print(dc[macloc][1])
        #check vector vs message for mac and ip match 
        if((searchLis(dc, clientMac)) == False):#True):
            print("server:Mac address in the list")
            
            #find location of macaddress in data container
            macloc = macLocate(dc, clientMac) 
        #check ip match
            if(dc[macloc][2] != rcvm[15:-9]):
        #if check fails send decline message 
                print("server:IP Addresses don't match Decline message")
                declineMessage = '7:server: Decline Server records error'
                serverSocket.sendto(declineMessage.encode(), clientAddress)
        #else check timestamp is valid
            else:
                if(timeCheck(rcvm[-8:]) != True):
                    print("server:Time stamp not valid Decline message")
                    declineMessage = '7:server: Decline Time stamp expired'
                    serverSocket.sendto(declineMessage.encode(), clientAddress)
                #if timestamp expired send decline
                
                
                else:
                    dc[macloc][4] = True
                    print("server:Sending Acknowledgement Message")
                    #else server set acked field to True
                    anAck = [dc[macloc][1], dc[macloc][2], dc[macloc][3]]
                    panAck = addackPre(anAck)
                    #print(panAck)
                    serverSocket.sendto(panAck.encode(), clientAddress)
          #then send acknowledge message w/ mac ip & timestamp
            
    elif(rcvm[0] == '3'):
        print("server:Acknowledge message received")
        
    elif(rcvm[0] == '4'):
        print("server:Release message received")
        relMes= rcvm[2:]
        relMac = rcvm[2:14]
        print(relMes)
        print(relMac)
        #if the macaddr is not in the data container dc do nothing
        if((searchLis(dc, relMes[2:14]))==True):#False):
            '''
            relmacloc = 0
            for mpos in range(0,14):
                if(relMac == dc[mpos][1]):
                    relmacloc = mpos
            
                        
            #relmacloc = macLocate(dc, relMac)
            dc[relmacloc][1] = '0'
            dc[relmacloc][3] = aCloc.strftime("%X")
            dc[relmacloc][4] = False
            #clearing out mac's ip assignment
            print(dc[relmacloc])
            #decrease the 
            mypoolSize = mypoolSize -1
            '''
            pass
            
        #else mac is in list find location
        else:
            
            relmacloc = 0
            
            for mpos in range(0,14):
                if(relMac == dc[mpos][1]):
                    relmacloc = mpos
            
                        
            #relmacloc = macLocate(dc, relMac)
            dc[relmacloc][1] = '0'
            dc[relmacloc][3] = aCloc.strftime("%X")
            dc[relmacloc][4] = False
            #clearing out mac's ip assignment
            print(dc[relmacloc])
            #decrease the 
            mypoolSize = mypoolSize -1
            
    elif(rcvm[0] == '5'):
        print("server:Renew message received")
        
        renMes = rcvm[2:]
        renMac = rcvm[2:14]
        print(renMes)
        
        #check vector for macaddr
        if(searchLis(dc, renMac[2:14])==False):
            renmacloc = 0
            for npos in range(0,14):
                if(renMac == dc[npos][1]):
                    renmacloc = npos
        
            dc[renmacloc][1] = renMac
            dc[renmacloc][3] = timeStamp()
            dc[renmacloc][4] = True
            #clearing out mac's ip assignment
            print(dc[renmacloc])
            
            print("server:Sending Acknowledgement Message")
            #else server set acked field to True
            nAck = [dc[renmacloc][1], dc[renmacloc][2], dc[renmacloc][3]]
            pnAck = addackPre(nAck)
            #print(panAck)
            serverSocket.sendto(pnAck.encode(), clientAddress)
            #then send acknowledge message w/ mac ip & timestamp

        #if mac address wasnt in list
        elif(searchLis(dc, renMes[2:14])==True):
            #
            if(poolCheck(mypoolSize)==False): #if ipaddr pool is not full
            
            
                mypoolSize = incPoolSize(mypoolSize)
                clientIP = ipGrab(mypoolSize)
                newD = [renMac, clientIP, timeStamp()]                
                
                #Storing vector element data
                #dc[mypoolSize-1][0] = mypoolSize -1 #% 14
                dc[mypoolSize-1][1] = newD[0] #clientMac
                dc[mypoolSize-1][2] = newD[1]
                dc[mypoolSize-1][3] = newD[2]
                dc[mypoolSize-1][4] = False
                                
                print("server:Pool not yet full new data being entered:")
                print(newD)
                offMess = addofferPre(newD)
                print("server:Offer Message Being Sent")
                print(offMess)
                serverSocket.sendto(offMess.encode(), clientAddress)                        
                        
            elif(poolCheck(mypoolSize) == True): #if pool is full
                #checks the vector timestamps
                
                sRes = 0
                for mpos in range(0,14):
                    if(aCloc.strftime("%X") > dc[mpos][3]):
                        sRes = mpos
                    else:
                        sRes = -1
                          
                
                '''stamResult = timeStampCheck(dc)
                #if a record has expired use that ipaddr    
                if (stamResult != -1 ):
                    
                    newVecData = [stamResult, renMac, dc[stamResult][2], timeStamp()]
                    dc[stamResult][0] = stamResult #+ 1
                    dc[stamResult][1] = newVecData[1]#clientMac
                    dc[stamResult][2] = newVecData[2]
                    dc[stamResult][3] = newVecData[3]
                    dc[stamResult][4] = False
                '''
                #if a record has expired use that ipaddr    
                if (sRes != -1 ):
                    newVecData = [sRes, clientMac, dc[sRes][2], timeStamp()]
                    #dc[sRes][0] = sRes #+ 1
                    dc[sRes][1] = newVecData[1]#clientMac
                    dc[sRes][2] = newVecData[2]
                    dc[sRes][3] = newVecData[3]
                    dc[sRes][4] = False 
                    #expired time offer message
                    exptoffmess = addofferPre(newVecData)
                    print(extoffmess)
                    serverSocket.sendto(extoffmess.encode(), clientAddress)
                
                else:
                    #if list occupied fully & no record expired
                    #decline request and send decline message
                    print("server:Pool full declining request and sending DECLINE message")
                    declineMessage = '9:404:server: DDoS Server not found'
                    serverSocket.sendto(declineMessage.encode(), clientAddress)

                  
        
    elif(rcvm[0] == '6'):
        print("server:List message received")
        adc = ""
        amyLis = []
        for count in range(0,14):
            myLis = [ dc[count][0],  dc[count][1],  dc[count][2],  dc[count][4]    ]
            amyLis.append(myLis)
            #addLis = 
        
        adc = ' '.join(map(str,amyLis))
            
        serverSocket.sendto(adc.encode(), clientAddress)
'''
    #pull mac address from discover message
    aMac = macPull(message.decode()[2:])
    #print(ipGrab(ipAssignCheck(aMac)))
    modifiedMessage = message.decode()[2:].upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
'''        
    
    
    
    
    
    
    
