import random
import time

from paho.mqtt import client as mqtt_client
BROKER = "10.21.160.16"
PORT = 1883
topic = "Test"

client_id = f"python-mqtt-{random.randint(0, 1000)}"

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(BROKER, PORT)
    return client

def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"counter: {msg_count}"
        result = client.publish(topic, msg)
        status = result[0]
        if status == 0:
            print(f"Send {msg} to topic {topic}")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1