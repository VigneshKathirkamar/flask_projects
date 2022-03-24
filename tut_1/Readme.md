# Deploying flask app to GCP

## Part 1 :

First create a simple flask web app (like addition of two numbers by getting input from user)

## Part 2:

Pre-requisites:
- Billing enabled GCP project (Projects created in trial version also supports billing)
- glcoud sdk installed locally
- make sure you name your python file as `main.py`

Create the necessay files such as "requirements.txt" and "app.yaml"

Go to the root folder where the files reside and run
```
gcloud auth login
gcloud config set project <put your project id here>
gcloud app deply
```


