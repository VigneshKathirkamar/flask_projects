FROM python:3.7

# making a directory called /app 
RUN mkdir /app  

# setting the working directory to be /app/
WORKDIR /app/

# Adding all our files from present folder to /app/
ADD . /app/

# Running pip install command to get our required libaries
RUN pip install -r requirements.txt

# Run the app finally
CMD ["python","/app/main.py"]