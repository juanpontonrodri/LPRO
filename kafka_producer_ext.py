from kafka import KafkaProducer
import json
import random
import time

# Configura el productor de Kafka
producer = KafkaProducer(
    bootstrap_servers=['172.18.0.2:31090'],
    security_protocol="SASL_PLAINTEXT",
    sasl_mechanism="SCRAM-SHA-256",
    sasl_plain_username="user1",
    sasl_plain_password="WVlCagOjSj",
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Función para generar mensajes aleatorios
def generate_random_message():
    return {
        'id': random.randint(1, 1000),
        'value': random.random()
        #return random.randint(1, 1000) + ',' + random.random()

    }

# Envía mensajes aleatorios al topic
topic_name = 'test'
try:
    for _ in range(100):  # Cambia 100 por el número de mensajes que quieras enviar
        message = generate_random_message()
        producer.send(topic_name, value=message)
        print(f"Sent: {message}")
        #time.sleep(1)  # Espera 1 segundo entre mensajes para hacerlo más legible
finally:
    producer.flush()
    print("Finished sending messages.")