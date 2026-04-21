# ---------- MQTT client ----------
# Install MQTT client on your IoT-unit
# To do this you first need an internet connection
#>>> import mip
#>>> mip.install(’umqtt.robust’)
#>>> mip.install(’umqtt.simple’)


# ---------- Publisher 2 ----------
# Read IoT-data and publish to broker/HiveMQ
# MicroPython

import network
import time 
from umqtt.simple import MQTTClient
from machine import Pin
import dht
import utime

# WiFi
ssid = "Mindpark Guest"
password = "SipAndSurf!"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected():
    time.sleep(1)

print("Connected to WiFi")

# MQTT
broker = "4cfe7cae48cb4e3581a1905ef84d6038.s1.eu.hivemq.cloud"
server_hostname = "4cfe7cae48cb4e3581a1905ef84d6038.s1.eu.hivemq.cloud"
port = 8883
username = "hivemq.webclient.1776763220143"
password = "6l57hxH<M2?zKVfQw:&G"
topic = "room1/environment"

def connectMQTT():
    client = MQTTClient(client_id=b"pico_1",
         server=broker,
         port=port,
         user=username,
         password=password,
         keepalive=7200,
         ssl=True,
         ssl_params={'server_hostname': server_hostname})
    client.connect()
    return client

client = connectMQTT()

# Sensor (placeholder)
# https://docs.micropython.org/en/latest/library/machine.Pin.html#machine-pin

sensor = dht.DHT11(machine.Pin(28))
pin_value = sensor.value()

# Skicka data
def publish(topic, value):
    print(topic)
    print(value)
    client.publish(topic, value)
    print("Publish done")
    
while True:
    publish(topic,str(pin_value))
    time.sleep(2)



