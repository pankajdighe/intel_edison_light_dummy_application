import time
import paho.mqtt.client as mqtt
import random

mqttc=mqtt.Client()
mqttc.connect("iot.eclipse.org",1883,60)
mqttc.loop_start()

#read light

def read_light_data():
    return random.randint(30, 70)

#publish temperature
while 1:
    t=read_light_data()
    (result,mid)=mqttc.publish("topic/GeneralizedIoT/light",t,2)
    time.sleep(1)

mqttc.loop_stop()
mqttc.disconnect()