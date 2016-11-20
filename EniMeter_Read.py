# Script written by - Naman & Yash
# Place: IIT Gandhinagar, India

import minimalmodbus
import time
import datetime
import os.path
import csv
from math import ceil
import decimal

#----------   
comchannel = minimalmodbus.Instrument('COM3',1) #Port Name as per the machine; "/dev/ttyUSB0" - for Raspberry Pi"; If IOError check if the MODBUS ADDRESS (here 1) is correct or not at the EniConnect Terminal   
comchannel.serial.baudrate = 9600 # Working at baudrate 9600 - Keep it same for at both the places (Settings as well as here)
comchannel.serial.timeout = 4 # In seconds - Timeout increased to prevent the crashing that was happening due to very less timeout value
#datascalar = 1 # Initializing the datascalar variable

#timeinterval = 1 # Time in seconds after which we want to again collect the values for all the parameters
wait=0.01 # Wait between 2 successive values to be taken from the meter
errorwait=0.1 # Waittime once an error occurs


#value_address = 0.0
#----------

#----------
# DataScalars - Write whatever data scalar you want from each channel in the following datascalar assignments - By default 1

##datascalar1=1
##datascalar2=1
##datascalar3=1
##datascalar4=1
##
##
##comchannel.write_register(40103,datascalar1)
##time.sleep(wait)
##comchannel.write_register(40203,datascalar2)
##time.sleep(wait)
##comchannel.write_register(40303,datascalar3)
##time.sleep(wait)
##comchannel.write_register(40403,datascalar4)
##time.sleep(wait)
#----------  

##comchannel.write_register(40202,150)
##print comchannel.read_register(40102)
##time.sleep(1)
##print comchannel.read_register(40202)

def portopening():
#    ioError += 1
    comchannel = minimalmodbus.Instrument('COM3',1) #Port Name as per the machine; "/dev/ttyUSB0" - for Raspberry Pi"; If IOError check if the MODBUS ADDRESS (here 1) is correct or not at the EniConnect Terminal   
    comchannel.serial.baudrate = 9600 # Working at baudrate 9600 - Keep it same for at both the places (Settings as well as here)
    comchannel.serial.timeout = 1 # In seconds - Timeout increased to prevent the crashing that was happening due to very less timeout value
    time.sleep(wait)
##    comchannel.read_register(40103,1) # To clear the buffer the following unnecessary reading of registers done 
##    time.sleep(wait)
##    comchannel.read_register(40203,1)
##    time.sleep(wait)
##    comchannel.read_register(40303,1)
##    time.sleep(wait)
##    comchannel.read_register(40403,1)

    data = [0.0]*15
    return data


#------------------------------------
 #Lists to contain the values
#channel10values=[0.0]*40
channel1values=[0.0]*11
channel2values=[0.0]*11
channel3values=[0.0]*11
channel4values=[0.0]*11
#------------------------------------

#------------------------------------
    #Register address lists - Refer Documentation for the meaning of these addresses

#channel10address = [40164, 40165, 40166, 40167, 40168, 40169, 40170, 40171, 40172, 40173, 40264, 40265, 40266, 40267, 40268, 40269, 40270, 40271, 40272, 40273, 40364, 40365, 40366, 40367, 40368, 40369, 40370, 40371, 40372, 40373, 40464, 40465, 40466, 40467, 40468, 40469, 40470, 40471, 40472, 40473]


channel1address = 40164
channel2address = 40264
channel3address = 40364 
channel4address = 40464

#------------------------------------


#------------------------------------
# Function to get the values from the MODBUS RTU protocol

##def getvalue(address):
##    
##    
##    #start = time.clock()
##    #if number in [64,65,66]:
##    
##    
##    value_address = comchannel.read_registers(address,10)
##    
##    #print stop
##    #stop = time.clock()- start
##    #print 'stop', stop
##    #elif number in [67,68,69]:
##        #value_address = comchannel.read_register(address,1,signed=True)
##
##    #elif number in [70,71,72,73]:
####        if datascalar == 0:
####            value_address = comchannel.read_register(address,3,signed=True)
##        #elif datascalar == 1:
##         #   value_address = comchannel.read_register(address,2,signed=True)
##        #elif datascalar == 2:
##         #   value_address = comchannel.read_register(address,1,signed=True)
##        #elif datascalar == 3:
##         #   value_address = comchannel.read_register(address,0,signed=True)        
##    #stop = time.clock()- start
##    #print 'stop', stop
##    return value_address

#------------------------------------

    
#------------------------------------
# Lists containing the values are updated here


def getchannels():
    
    try:

        #print "-------------------------"  
        #print "Getting channel 1 values:"
           
        
        channel1values = comchannel.read_registers(channel1address,11)
        time.sleep(wait)
        channel1values = [ ceil((x/100.0)*100)/100 for x in channel1values ]
        channel1values[3:6] = [ x*10 for x in channel1values[3:6] ]
        
        #print channel1values


        channel2values = comchannel.read_registers(channel2address,11)
        time.sleep(wait)
        channel2values = [ ceil((x/100.0)*100)/100 for x in channel2values ]
        channel2values[3:6] = [ x*10 for x in channel2values[3:6] ]

        channel3values = comchannel.read_registers(channel3address,11)
        time.sleep(wait)
        channel3values = [ ceil((x/100.0)*100)/100 for x in channel3values ]
        channel3values[3:6] = [ x*10 for x in channel3values[3:6] ]

        channel4values = comchannel.read_registers(channel2address,11)
        time.sleep(wait)
        channel4values = [ ceil((x/100.0)*100)/100 for x in channel4values ]
        channel4values[3:6] = [ x*10 for x in channel4values[3:6] ]
        

        A = map(str, channel1values)
        A.extend([''])
    
    
        B = map(str, channel2values)
        B.extend([''])

        C = map(str, channel3values)
        C.extend([''])

        D = map(str, channel4values)
        D.extend([''])

        T = [str(t+1)]
        T.extend([' '])

        

        data = T + A + [time.clock()] + [time.asctime( time.localtime(time.time()) )]#

        
        #print channel4values
        #time.sleep(wait)
        #print channel1values
        #print "Channel 1 Values updated!"
        
    except IOError:
        
        print "\\\\IOError Occured////"
        data = portopening()
        time.sleep(errorwait)
    
    return data

#----------
def write(t, day):
    
    fileName = os.path.join('./Data', "File - " + str(day) +".csv")
    if not os.path.exists(os.path.dirname(fileName)):
        os.makedirs(os.path.dirname(fileName))
    with open(fileName, 'ab') as csvfile:
        writer =csv.writer(csvfile)
        writer.writerow(data)
                           
#------------------------------------
 #Infinite loop to continuously call the functions to get the values after specific time interval
#global ioError
#ioError = 0
name = datetime.datetime.now().strftime('%d %B %Y, %H-%M-%S')
##cumTime = 0
while True:
    t=0
    for t in range (15200) :
##        start = time.clock()
        data = getchannels()
        write(t, name)
        
        t += 1
##        stop = time.clock() - start
##        cumTime += stop
##        print 'Time', stop, 'CumTime',cumTime,'Hour',day
        print "Keep Calm, Hakuna Matata ...", t
    name = datetime.datetime.now().strftime('%d %B %Y, %H-%M-%S')
#print ioError
#------------------------------------

