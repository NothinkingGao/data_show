from datetime import datetime
from flask import Flask, render_template as template
from pandas import read_csv
from flask import jsonify
import numpy as np
import config
import bll
from bll import get_weather_by_date
from flask import request

# set the url_for host to the local ip address
# set the static_url_path to the local ip address
app = Flask(__name__)

@app.route("/time")
def server_time():
    return "Server time is: " + str(datetime.now())

@app.route("/ping")
def ping():
    return "pong"

@app.route("/data")
def return_csv():
    return read_csv("data.csv")

# receive json parame and get weather data by date
@app.route("/weather", methods=["POST"])
def weather():
    start_date_time = request.form.get("startDatetime")
    end_date_time = request.form.get("endDatetime")
    weather_data = get_weather_by_date(start_date_time,end_date_time)
    # convert weather object list to json list
    weather_json = []
    for weather in weather_data:
        weather_json.append(weather.to_dict())
    return jsonify(weather_json)

# get population data by city,default city is 0
@app.route("/population", methods=["POST"])
def population():
    city = request.form.get("cityId")
    population_data = bll.get_population_by_city(city)
    # convert population object list to json list
    population_json = []
    for population in population_data:
        population_json.append(population.to_dict())
    return jsonify(population_json)

# get all industrial data
@app.route("/industrial", methods=["POST"])
def industrial():
    industrial_data = bll.get_industrial_production()
    # convert industrial object list to json list
    industrial_json = []
    for industrial in industrial_data:
        industrial_json.append(industrial.to_dict())
    return jsonify(industrial_json)

# get all finance data
@app.route("/finance", methods=["POST"])
def finance():
    finance_data = bll.get_finance()
    # convert finance object list to json list
    finance_json = []
    for finance in finance_data:
        finance_json.append(finance.to_dict())
    return jsonify(finance_json)

@app.route("/data/<int:row>")
def get_row(row):
    return read_csv(f"{config.DATA_DIRECTORY}/weather.csv").iloc[row]

@app.route("/")
def hello_world():
    return template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000, debug=True)
