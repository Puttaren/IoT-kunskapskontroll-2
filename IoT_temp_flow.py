import network
import time
import dht
import ujson
from machine import Pin
from umqtt.simple import MQTTClient

# WiFi
ssid = "Mindpark Guest"
wifi_password = "SipAndSurf!"

# MQTT
broker = "4cfe7cae48cb4e3581a1905ef84d6038.s1.eu.hivemq.cloud"
server_hostname = broker
port = 8883
username = "hivemq.webclient.1776763220143"
mqtt_password = "6l57hxH<M2?zKVfQw:&G"
topic = b"room1/environment"

# Sensor
sensor = dht.DHT11(Pin(28))

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, wifi_password)

    print("Connecting to WiFi...")
    timeout = 15
    while not wlan.isconnected() and timeout > 0:
        time.sleep(1)
        timeout -= 1

    if wlan.isconnected():
        print("Connected to WiFi")
        print(wlan.ifconfig())
        return wlan
    else:
        raise Exception("WiFi connection failed")

def connect_mqtt():
    client = MQTTClient(
        client_id=b"pico_1",
        server=broker,
        port=port,
        user=username,
        password=mqtt_password,
        keepalive=7200,
        ssl=True,
        ssl_params={"server_hostname": server_hostname}
    )
    client.connect()
    print("Connected to MQTT")
    return client

LOW_TEMP = 20
HIGH_TEMP = 23

def classify_temperature(temp):
    if temp < LOW_TEMP:
        return "fan_warm"
    elif temp > HIGH_TEMP:
        return "fan_cold"
    else:
        return "off"

def publish_sensor_data(client):
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()

        temp_status = classify_temperature(temp)

        payload = ujson.dumps({
            "temperature": temp,
            "humidity": hum,
            "temp_status": temp_status
        })

        client.publish(topic, payload)
        print("Published:", payload)

    except OSError:
        print("Kunde inte läsa från sensorn")


# Main
connect_wifi()
client = connect_mqtt()

while True:
    publish_sensor_data(client)
    time.sleep(2)

