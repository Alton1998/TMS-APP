import paho.mqtt.client as mqtt #import the client1
import time
import math
from tmsapp.models import trafficAtD,trafficAtC,trafficAtB,trafficAtA
############
########################################
broker_address="172.16.73.4"
#broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("P1") #create new instance
print("connecting to broker")
client.connect(broker_address) #connect to broker
while True:
    DATA = trafficAtA.objects.all().order_by('id')
    DATA1 = trafficAtB.objects.all().order_by('id')
    DATA2 = trafficAtC.objects.all().order_by('id')
    DATA3 = trafficAtD.objects.all().order_by('id')
    DATAREV = DATA.reverse()[:1]
    for k in DATAREV:
        a = math.floor(k.Trafficdensity)
    DATAREV1 = DATA1.reverse()[:1]
    for k in DATAREV1:
        l = math.floor(k.Trafficdensity)
    DATAREV2 = DATA2.reverse()[:1]
    for k in DATAREV2:
        c = math.floor(k.Trafficdensity)
    DATAREV3 = DATA3.reverse()[:1]
    for k in DATAREV3:
        d = math.floor(k.Trafficdensity)
    client.loop_start() #start the loo
    print("Publishing message to topic","Signal")
    if (a+c)>(l+d):
        client.publish("SignalAtAGreen/","On")
        client.publish("SignalAtARed/","Off")
        client.publish("SignalAtAYellow/","Off")
        client.publish("SignalAtBGreen/", "Off")
        client.publish("SignalAtBRed/", "On")
        client.publish("SignalAtBYellow/", "Off")
        client.publish("SignalAtCGreen/", "On")
        client.publish("SignalAtCRed/", "Off")
        client.publish("SignalAtCYellow/", "Off")
        client.publish("SignalAtDGreen/", "Off")
        client.publish("SignalAtDRed/", "Off")
        client.publish("SignalAtDYellow/", "Off")
    elif (l+d)>(a+c):
        client.publish("SignalAtAGreen/", "Off")
        client.publish("SignalAtARed/", "On")
        client.publish("SignalAtAYellow/", "Off")
        client.publish("SignalAtBGreen/", "On")
        client.publish("SignalAtBRed/", "Off")
        client.publish("SignalAtBYellow/", "Off")
        client.publish("SignalAtCGreen/", "Off")
        client.publish("SignalAtCRed/", "On")
        client.publish("SignalAtCYellow/", "Off")
        client.publish("SignalAtDGreen/", "On")
        client.publish("SignalAtDRed/", "Off")
        client.publish("SignalAtDYellow/", "Off")
    else:
        client.publish("SignalAtAGreen/", "Off")
        client.publish("SignalAtARed/", "Off")
        client.publish("SignalAtAYellow/", "On")
        client.publish("SignalAtBGreen/", "Off")
        client.publish("SignalAtBRed/", "Off")
        client.publish("SignalAtBYellow/", "On")
        client.publish("SignalAtCGreen/", "Off")
        client.publish("SignalAtCRed/", "Off")
        client.publish("SignalAtCYellow/", "On")
        client.publish("SignalAtDGreen/", "Off")
        client.publish("SignalAtDRed/", "Off")
        client.publish("SignalAtDYellow/", "On")
    time.sleep(4)