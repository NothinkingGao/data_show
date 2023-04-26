from dll.weather import Weather

# open datas/weather.csv and input the data to the database
def import_weather_data():
    with open(f"{config.DATA_DIRECTORY}/weather.csv", "r") as file:
        for line in file:
            data = line.split(",")
            date = data[0]
            high_temp = data[1]
            low_temp = data[2]
            weather = data[3]
            wind_direction = data[4]
            wind_power = data[5]
            air_index = data[6]
            air_info = data[7]
            air_level = data[8]
            weather = Weather(date, high_temp, low_temp, weather, wind_direction, wind_power, air_index, air_info, air_level)
            session.add(weather)
        session.commit()