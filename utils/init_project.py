import sys
import os
sys.path.append("..")
import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from sqlalchemy.ext.declarative import declarative_base
from dll.weather import Weather
import numpy as np
from logging_config import logger


# create session
engine = create_engine(f'mysql+pymysql://{config.MYSQL_USER}:{config.MYSQL_PASSWORD}@{config.MYSQL_HOST}'
                          f':{config.MYSQL_PORT}/{config.DATABASE}?charset=utf8')

Session = sessionmaker(bind=engine)

# create database my_statistic use python
def create_database():
    engine = create_engine(f'mysql+pymysql://{config.MYSQL_USER}:{config.MYSQL_PASSWORD}@{config.MYSQL_HOST}'
                           f':{config.MYSQL_PORT}/?charset=utf8')
    conn = engine.connect()
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {config.DATABASE} DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci"))
    conn.close()
    engine.dispose()



# read weather.csv  by numpy and input the data to the weather table
def import_weather_data():
    # create session
    session = Session()
    # read weather.csv
    data = np.loadtxt(f"{config.BASE_DIR}/datas/weather.csv", dtype=str, delimiter=",", skiprows=1,encoding='utf-8')
    # input the data to the weather table
    for line in data:
        logger.info(line)
        date = line[0]
        high_temp = int(line[1].replace("°",""))
        low_temp = int(line[2].replace("°",""))
        weather = line[3]
        wind_direction = line[4]
        wind_power = line[5]
        air_index = int(line[6]) if line[6] else 0
        air_info = line[7]
        air_level = line[8]
        weather = Weather(date, high_temp, low_temp, weather, wind_direction, wind_power, air_index, air_info, air_level)
        session.add(weather)
    session.commit()



if __name__ == '__main__':
    create_database()
    import_weather_data()