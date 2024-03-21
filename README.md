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

helm install mi-kafka bitnami/kafka -f https://raw.githubusercontent.com/juanpontonrodri/LPRO/main/kafka-values.yaml
```

## Testing 
Simple test with kafka-client pod:
