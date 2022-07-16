from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, How are you buddy?"

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
    # "0.0.0.0", tells a server to "listen" for and accept connections from any IP address. 