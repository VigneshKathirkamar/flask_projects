# "Hello World" in Kubernetes

## Build docker image:
```
sudo docker build -t hello-world .
```
## Tag docker image:
```
sudo docker login
```
enter unmae and password

```
sudo docker tag <docker image name>:<tag> <docker user id>/<some tag name>
```
Eg:
sudo docker tag hello_world:latest vigneshkathirkamar/firstimage

## Push to docker hub:

sudo docker push vigneshkathirkamar/firstimage

## Create deployment file (manifest)
Create a yaml file containing the details of the deployment

## Create service file (manifest)
Create a yaml file containing the details of the service

Error: Failed to pull image
minikube cache add vigneshkathirkamar/firstimage

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

minikube service flask-service
