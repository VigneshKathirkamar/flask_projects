from distutils.log import debug
from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/',methods=["POST","GET"])
def home():
    sum = ''
    first_num = 0
    second_num = 0
    try:
        if request.method == "POST" and 'first_num' in request.form and 'second_num' in request.form:
            first_num = int(request.form.get('first_num'))
            second_num = int(request.form.get('second_num'))
            sum = float(first_num + second_num)
    except Exception as e:
        print("Error occured:",e)
    return render_template('index.html',sum=sum,first_num=first_num,second_num=second_num)

if __name__ == "__main__":
    app.run(debug=True)