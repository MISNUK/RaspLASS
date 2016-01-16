import paho.mqtt.client as mqtt
MQTT_SERVER = "140.127.220.46"
MQTT_PORT = 1883
MQTT_ALIVE = 60
MQTT_TOPIC = "LASS/Test/PM25"

##-----------------
def on_connect(client, userdata, rc):
    print("MQTT Connected with result code "+str(rc))
    client.subscribe(MQTT_TOPIC)
def on_disconnect(client, userdata, msg):
    print >>sys.stderr, "NOTICE: Disconnected"
    client.unsubscribe(MQTT_TOPIC)
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


##-----------------------
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_SERVER, MQTT_PORT, MQTT_ALIVE)
#subscribe(MQTT_TOPIC, qos=0)
client.loop_forever()
