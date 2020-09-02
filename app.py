from flask import Flask, render_template, request, redirect
import requests
import datetime
import sys

app = Flask(__name__)

username = ""

vehiculeList = []

@app.route("/")
def index():
    return render_template('index.html', username = username)

@app.route("/userlogin", methods=["GET","POST"])
def userlogin():
    if request.method == "POST":
        req = request.form
        username = req['username']
        print(username)
        redirect(request.url)
        if username == "client":
            vehiculeList = fillVehiculeList()
            return render_template('vehiculeslist.html', username = username, vehiculeList = vehiculeList)
        if username == "vendeur":
            return render_template('dashboard.html', username = username)
        if (username != 'vendeur' and username != "client"):
            return render_template('authenticationfailed')
    return render_template('userlogin.html')

@app.route("/vehicules")
def vehicules():
    vehiculeList = fillVehiculeList()
    print(vehiculeList)
    return render_template('vehiculeslist.html', username = username, vehiculeList = vehiculeList)

@app.route("/visiteVirtuelle")
def visiteVirtuelle():
    return render_template('visiteVirtuelle.html', username = username)

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html', username = username)

def fillVehiculeList():
    data = []
    maker = "BMW"
    model = "série 1"
    mileage = 130000
    data.append((maker, model, mileage))
    maker = "BMW"
    model = "X5"
    mileage = 145028
    data.append((maker, model, mileage))
    maker = "Volkswagen"
    model = "Golf"
    mileage = 10000
    data.append((maker, model, mileage))
    maker = "Nissan"
    model = "Juke"
    mileage = 237644
    data.append((maker, model, mileage))
    return data

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
