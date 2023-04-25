import sys
import os
sys.path.append("..")
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey,Float
from sqlalchemy.ext.declarative import declarative_base
import config

Base = declarative_base()

# 创建一个sqlalchemy的对象，对象拥有属性：日期,最高气温,最低气温,天气,风向,风力,空气指数,空气信息,空气等级)
class Weather(Base):
    __tablename__ = "weather"
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    high_temp = Column(Integer)
    low_temp = Column(Integer)
    weather = Column(String(255))
    wind_direction = Column(String(255))
    wind_power = Column(String(255))
    air_index = Column(Integer)
    air_info = Column(String(255))
    air_level = Column(String(255))

    def __init__(self, date, high_temp, low_temp, weather, wind_direction, wind_power, air_index, air_info, air_level):
        self.date = date
        self.high_temp = high_temp
        self.low_temp = low_temp
        self.weather = weather
        self.wind_direction = wind_direction
        self.wind_power = wind_power
        self.air_index = air_index
        self.air_info = air_info
        self.air_level = air_level

    def __repr__(self):
        return "<Weather(date='%s', high_temp='%s', low_temp='%s', weather='%s', wind_direction='%s', wind_power='%s', air_index='%s', air_info='%s', air_level='%s')>" % (
            self.date, self.high_temp, self.low_temp, self.weather, self.wind_direction, self.wind_power, self.air_index, self.air_info, self.air_level)

    def __str__(self):
        return "Weather(date='%s', high_temp='%s', low_temp='%s', weather='%s', wind_direction='%s', wind_power='%s', air_index='%s', air_info='%s', air_level='%s')" % (
            self.date, self.high_temp, self.low_temp, self.weather, self.wind_direction, self.wind_power, self.air_index, self.air_info, self.air_level)

    def __unicode__(self):
        return "Weather(date='%s', high_temp='%s', low_temp='%s', weather='%s', wind_direction='%s', wind_power='%s', air_index='%s', air_info='%s', air_level='%s')" % (
            self.date, self.high_temp, self.low_temp, self.weather, self.wind_direction, self.wind_power, self.air_index, self.air_info, self.air_level)
    
    def to_dict(self):
        return {
            "date": self.date,
            "high_temp": self.high_temp,
            "low_temp": self.low_temp,
            "weather": self.weather,
            "wind_direction": self.wind_direction,
            "wind_power": self.wind_power,
            "air_index": self.air_index,
            "air_info": self.air_info,
            "air_level": self.air_level
        }

# 创建一个sqlalchemy的对象，拥有：“城市”,"年份","常住人口(万人)“字段,常住人口是一个浮点数
class Population(Base):
    __tablename__ = "population"
    id = Column(Integer, primary_key=True)
    city = Column(String(255))
    year = Column(Integer)
    population = Column(Float)

    def __init__(self, city, year, population):
        self.city = city
        self.year = year
        self.population = population

    def __repr__(self):
        return "<Population(city='%s', year='%s', population='%s')>" % (
            self.city, self.year, self.population)

    def __str__(self):
        return "Population(city='%s', year='%s', population='%s')" % (
            self.city, self.year, self.population)

    def __unicode__(self):
        return "Population(city='%s', year='%s', population='%s')" % (
            self.city, self.year, self.population)

    def to_dict(self):
        return {
            "city": self.city,
            "year": self.year,
            "population": self.population
        }

# 创建一个sqlalchemy的对象:工业生产值，拥有：“年份”,"生产值",生产值是一个浮点数
class IndustrialProduction(Base):
    __tablename__ = "industrial_production"
    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    production = Column(Float)

    def __init__(self, year, production):
        self.year = year
        self.production = production

    def __repr__(self):
        return "<IndustrialProduction(year='%s', production='%s')>" % (
            self.year, self.production)

    def __str__(self):
        return "IndustrialProduction(year='%s', production='%s')" % (
            self.year, self.production)

    def __unicode__(self):
        return "IndustrialProduction(year='%s', production='%s')" % (
            self.year, self.production)

    def to_dict(self):
        return {
            "year": self.year,
            "production": self.production
        }


# 创建一个sqlalchemy的对象Finance,拥有:年份,金额,金额是一个浮点数
class Finance(Base):
    __tablename__ = "finance"
    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    money = Column(Float)

    def __init__(self, year, money):
        self.year = year
        self.money = money

    def __repr__(self):
        return "<Finance(year='%s', money='%s')>" % (
            self.year, self.money)

    def __str__(self):
        return "Finance(year='%s', money='%s')" % (
            self.year, self.money)

    def __unicode__(self):
        return "Finance(year='%s', money='%s')" % (
            self.year, self.money)

    def to_dict(self):
        return {
            "year": self.year,
            "money": self.money
        }

# create mysql database my_statistic.db
engine = create_engine(f'mysql+pymysql://{config.MYSQL_USER}:{config.MYSQL_PASSWORD}@{config.MYSQL_HOST}:{config.MYSQL_PORT}/my_statistic?charset=utf8')
Base.metadata.create_all(engine)
