from kafka import KafkaConsumer
import json

# Configuración del consumidor de Kafka
consumer = KafkaConsumer(
    'topic-test1',  # El nombre de tu topic
    bootstrap_servers=['kafka-controller-0.kafka-controller-headless.default.svc.cluster.local:9092',
                       'kafka-controller-1.kafka-controller-headless.default.svc.cluster.local:9092',
                       'kafka-controller-2.kafka-controller-headless.default.svc.cluster.local:9092'],
    security_protocol="SASL_PLAINTEXT",
    sasl_mechanism="SCRAM-SHA-256",
    sasl_plain_username="user1",
    sasl_plain_password="SASL_PASSWORD_PLACEHOLDER",
    auto_offset_reset='earliest',
    group_id='my-group',
    value_deserializer=lambda x: x.decode('utf-8')
)

print("Consumiendo mensajes de Kafka...")
for message in consumer:
    try:
        # Intenta deserializar el mensaje de JSON
        msg_data = json.loads(message.value)
        print(f"Mensaje recibido: {msg_data}")
    except json.JSONDecodeError:
        # Maneja el caso en que el mensaje no es JSON válido
        print(f"Mensaje no es JSON válido: {message.value}")