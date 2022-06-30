Build docker image:
docker build -t hello-world .


Tag docker image:

docker tag <docker image name>:<tag> <docker user id>/<some tag name>
Eg:
docker tag hello_world:latest vigneshkathirkamar/firstimage

Push to docker hub:
sudo docker push vigneshkathirkamar/firstimage


Create deployment file

Error: Failed to pull image
minikube cache add vigneshkathirkamar/firstimage

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

minikube service flask-service