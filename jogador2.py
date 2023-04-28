import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt

broker = "10.21.160.16"
port = 1883

TOPIC_PLAYER1 = "jogador1"

dica = input("Dica: ")

publish.single(TOPIC_PLAYER1, dica, hostname=broker, port=port)


def on_message(client, userdata, message):
    jogada1 = message.payload.decode()
    print(jogada1)


TOPIC_PLAYER2 = "jogador2"
client = mqtt.Client()
client.connect(broker, port)
client.subscribe(TOPIC_PLAYER2)

client.on_message = on_message
client.loop_forever()
