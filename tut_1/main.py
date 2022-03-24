from distutils.log import debug
from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/',methods=["POST","GET"])
def home():
    sum= ''
    if request.method == "POST" and 'first_num' in request.form and 'second_num' in request.form:
        first_num = float(request.form.get('first_num'))
        second_num = float(request.form.get('second_num'))
        sum = float(first_num + second_num)
    return render_template('index.html',sum=sum)

if __name__ == "__main__":
    app.run(debug=True)