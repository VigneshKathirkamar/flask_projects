# "Hello World" in Kubernetes

## Pre-requisites:
<ul>
<li> Docker installed </li>
<li>Account on docker hub</li>
<li>Minikube installed</li>
</ul>

## Some Useful commands:
<ol>
<li> Use `docker system prune -a --volumes` to delete all existing docker images </li>
</ol>

## Build docker image:
```
sudo docker build -t hello-world .
```
Used `sudo docker images` to check if the image is built

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

Error: Failed to pull image <br>
Fix: minikube cache add vigneshkathirkamar/firstimage

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

minikube start
(use command "minikube dashboard" to preview the kubernets dashboard UI)
minikube service flask-service
