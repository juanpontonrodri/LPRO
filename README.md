## PREVIOUS

Install kubectl and helm:
```
#kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
kubectl version --client
echo 'source <(kubectl completion bash)' >>~/.bashrc
source ~/.bashrc
 
#helm
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

Install kind if needed
```
#install homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
#follow steps at the end of previous command
 
brew install kind

kind create cluster
```

## Install kafka 
```
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update

helm install kafka bitnami/kafka -f kafka-values.yaml
```

## Testing 
Simple test with kafka-client pod following the steps after installation completed:

NOTE: change the password in the client.properties file to the one obtained by the command 
```
kubectl get secret kafka-user-passwords --namespace default -o jsonpath='{.data.client-passwords}' | base64 -d | cut -d , -f 1
```

```
kubectl run kafka-client --restart='Never' --image docker.io/bitnami/kafka:3.7.0-debian-12-r0 --namespace default --command -- sleep infinity
kubectl cp --namespace default client.properties kafka-client:/tmp/client.properties
kubectl exec --tty -i kafka-client --namespace default -- bash

PRODUCER:
        kafka-console-producer.sh \
            --producer.config /tmp/client.properties \
            --broker-list kafka-controller-0.kafka-controller-headless.default.svc.cluster.local:9092,kafka-controller-1.kafka-controller-headless.default.svc.cluster.local:9092,kafka-controller-2.kafka-controller-headless.default.svc.cluster.local:9092 \
            --topic test

CONSUMER:
        kafka-console-consumer.sh \
            --consumer.config /tmp/client.properties \
            --bootstrap-server kafka.default.svc.cluster.local:9092 \
            --topic test \
            --from-beginning
```

## Testing with python script
```
kubectl run python-kafka --image=python:3.9-slim --restart=Never --namespace=default --command -- sleep infinity



#execute the script to set the password and copy the files
chmod +x prepare_and_copy.sh
./prepare_and_copy.sh


#install kafka-python
kubectl exec -it python-kafka -- pip install kafka-python

#execute the scripts
kubectl exec -it python-kafka -- python /kafka_producer.py
kubectl exec -it python-kafka -- python /kafka_consumer.py
```
#debugging commands
```
kubectl exec -it python-kafka -- /bin/bash

```

