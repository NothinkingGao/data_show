import sys
import os
sys.path.append("..")
import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from sqlalchemy.ext.declarative import declarative_base
from dll.dal import Weather,Population,Finance
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


# push code to github
def push_code_to_github():
    os.system("git add .")
    os.system("git commit -m 'update'")
    os.system("git push origin master")


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

# read population.csv  by numpy and input the data to the population table
def import_population_data():
    # create session
    session = Session()
    # read population.csv
    data = np.loadtxt(f"{config.BASE_DIR}/datas/population.csv",dtype=str ,delimiter=",", skiprows=1,encoding='utf-8')
    # input the data to the population table
    for line in data:
        logger.info(line)
        city = 0
        year = int(line[1].replace('\"',''))
        population = float(line[2].replace('\"',''))
        population = Population(city,year, population)
        session.add(population)
    session.commit()

# read industrial.csv  by numpy and input the data to the industrial table
def import_industrial_data():
    # create session
    session = Session()
    # read industrial.csv
    data = np.loadtxt(f"{config.BASE_DIR}/datas/industrial.csv",dtype=str ,delimiter=",", skiprows=1,encoding='utf-8')
    # input the data to the industrial table
    for line in data:
        logger.info(line)
        year = int(line[1].replace('\"',''))
        industrial = float(line[2].replace('\"',''))
        industrial = Industrial(year, industrial)
        session.add(industrial)
    session.commit()

# read finance.csv  by numpy and input the data to the finance table
def import_finance_data():
    # create session
    session = Session()
    # read finance.csv
    data = np.loadtxt(f"{config.BASE_DIR}/datas/finance.csv",dtype=str ,delimiter=",", skiprows=1,encoding='utf-8')
    # input the data to the finance table
    for line in data:
        logger.info(line)
        year = int(line[1].replace('\"',''))
        finance = float(line[2].replace('\"',''))
        finance = Finance(year, finance)
        session.add(finance)
    session.commit()

def test_import_population_data():
    import_population_data()
    # create session
    session = Session()
    population_data = session.query(Population).all()
    for data in population_data:
        print(data)




if __name__ == '__main__':
    # create_database()
    # import_weather_data()
    #test_import_population_data()
    #import_industrial_data()
    import_finance_data()