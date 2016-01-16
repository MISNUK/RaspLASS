import serial
##ser = serial.Serial(3)
##ser.baudrate=9600
ser=serial.Serial("/dev/ttyUSB0", baudrate=9600)
while(True):
 token = ser.read(24)
 token_hex=token.encode('hex')
 print token_hex
 pm1_cf=int(token_hex[8]+token_hex[9]+token_hex[10]+token_hex[11],16)
 pm25_cf=int(token_hex[12]+token_hex[13]+token_hex[14]+token_hex[15],16)
 pm10_cf=int(token_hex[16]+token_hex[17]+token_hex[18]+token_hex[19],16)
 pm1=int(token_hex[20]+token_hex[21]+token_hex[22]+token_hex[23],16)
 pm25=int(token_hex[24]+token_hex[25]+token_hex[26]+token_hex[27],16)
 pm10=int(token_hex[28]+token_hex[29]+token_hex[30]+token_hex[31],16)
 print "pm1_cf: "+str(pm1_cf)
 print "pm25_cf: "+str(pm25_cf)
 print "pm10_cf: "+str(pm10_cf)
 print "pm1: "+str(pm1)
 print "pm25: "+str(pm25)
 print "pm10: "+str(pm10)

