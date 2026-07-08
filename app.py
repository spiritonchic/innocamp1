from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/forecast')
def forecast():
    return render_template("forecast.html", forecast="")

@app.route('/get_forecast', methods=['POST'])
def get_forecast():
    city = request.form['city']
    forecast = f"Прогноз погоды для {city}"
    return render_template("forecast.html", forecast=forecast)

app.run(debug=True)