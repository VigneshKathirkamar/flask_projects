from distutils.log import debug
from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/',methods=["POST","GET"])
def home():
    bmi= ''
    if request.method == "POST" and 'Weight' in request.form and 'Height' in request.form:
        Weight = float(request.form.get('Weight'))
        Height = float(request.form.get('Height'))
        bmi = round(Weight/((Height/100)**2),2)
    return render_template('index.html',bmi=bmi)

if __name__ == "__main__":
    app.run(debug=True)