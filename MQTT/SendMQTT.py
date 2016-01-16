import paho.mqtt.publish as publish
import time
import datetime
MQTT_SERVER = "140.127.220.46"
MQTT_PORT = 1883
MQTT_ALIVE = 60
#MQTT_TOPIC = "LASS/Test/PM25"
MQTT_TOPIC = "hanwei/test"

while(1):
# if ((int(time.time()) % 10) ==0):
   time.sleep( 5 )
   tf = str(datetime.datetime.now())
   print tf
   publish.single(MQTT_TOPIC, tf, port=MQTT_PORT, keepalive=MQTT_ALIVE, hostname=MQTT_SERVER)

