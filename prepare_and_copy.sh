#!/bin/bash

# Obtener la contraseña de Kafka
PASSWORD=$(kubectl get secret kafka-user-passwords --namespace default -o jsonpath='{.data.client-passwords}' | base64 -d | cut -d , -f 1)

# Reemplazar el marcador de posición en los scripts de Python con la contraseña real
sed "s/SASL_PASSWORD_PLACEHOLDER/$PASSWORD/g" kafka_producer.py > kafka_producer_temp.py
sed "s/SASL_PASSWORD_PLACEHOLDER/$PASSWORD/g" kafka_consumer.py > kafka_consumer_temp.py

# Copiar los scripts modificados al contenedor
kubectl cp kafka_producer_temp.py default/python-kafka:/kafka_producer.py
kubectl cp kafka_consumer_temp.py default/python-kafka:/kafka_consumer.py

# Limpieza: eliminar los archivos temporales
rm kafka_producer_temp.py kafka_consumer_temp.py
