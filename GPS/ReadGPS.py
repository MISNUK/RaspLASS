import serial
import pynmea2

ser=serial.Serial("/dev/ttyUSB1", baudrate=38400)
while(True):
 token = ser.readline()
 line = token.rstrip()
 if (line.find('$GPGGA')==0):
   #print line
   msg = pynmea2.parse(line)
   print msg
   print msg.timestamp
   print msg.lat 
   #print msg.latitude

