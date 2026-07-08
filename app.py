from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index2.html")

@app.route('/forecast')
def forecast():
    return render_template("forecast.html")

app.run(debug=True)