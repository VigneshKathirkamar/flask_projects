Build docker image:
sudo docker build -t hello-world .

sudo docker login
enter unmae and password

Tag docker image:

sudo docker tag <docker image name>:<tag> <docker user id>/<some tag name>
Eg:
sudo docker tag hello_world:latest vigneshkathirkamar/firstimage

Push to docker hub:
sudo docker push vigneshkathirkamar/firstimage


Create deployment file

Error: Failed to pull image
minikube cache add vigneshkathirkamar/firstimage

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

minikube service flask-service