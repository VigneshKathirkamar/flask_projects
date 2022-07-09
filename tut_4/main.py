from flask import Flask,jsonify
import time

app = Flask(__name__)

@app.route('/')
def home():
    # return jsonify({"Time:":time.time()})
    # return jsonify("Hello,how are you?")
    return "Hello, How are you buddy?"

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)