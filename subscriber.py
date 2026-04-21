import paho.mqtt.client as mqtt
import json
import csv
import os
from datetime import datetime

broker = "4cfe7cae48cb4e3581a1905ef84d6038.s1.eu.hivemq.cloud"
port = 8883
username = "hivemq.webclient.1776763220143"
password = "6l57hxH<M2?zKVfQw:&G"
topic = "room1/environment"

BASE_DIR = "C:\YA BI analyst\Kurser\BI25M AI & IoT\Kunskapskontroll 2\IoT-kunskapskontroll-2"
CSV_FILE = os.path.join(BASE_DIR, "sensor_data.csv")

# Skapa mappen om den inte finns
os.makedirs(BASE_DIR, exist_ok=True)

print("CSV sparas i:", CSV_FILE)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    client.subscribe(topic)

def save_to_csv(data):
    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)

        # Skriv header första gången
        if not file_exists:
            writer.writerow(["timestamp", "temperature", "humidity", "temp_status"])

        writer.writerow([
            datetime.now().isoformat(),
            data.get("temperature"),
            data.get("humidity"),
            data.get("temp_status")
        ])

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    print("Message:", message)

    try:
        data = json.loads(message)  # 🔥 konvertera JSON → dict
        save_to_csv(data)
        print("Saved to CSV")

    except Exception as e:
        print("Error parsing message:", e)

client = mqtt.Client()
client.username_pw_set(username, password)
client.tls_set()

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port, 60)
client.loop_forever()