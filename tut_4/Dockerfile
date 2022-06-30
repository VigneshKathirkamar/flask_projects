FROM python:3.7

RUN mkdir /app

# ENV APP_HOME /app

WORKDIR /app/

ADD . /app/

RUN pip install -r requirements.txt

CMD ["python","/app/main.py"]