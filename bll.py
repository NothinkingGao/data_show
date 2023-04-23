from dll.weather import Weather
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import config

# create session
engine = create_engine(f'mysql+pymysql://{config.MYSQL_USER}:{config.MYSQL_PASSWORD}@{config.MYSQL_HOST}'
                          f':{config.MYSQL_PORT}/{config.DATABASE}?charset=utf8',pool_size=50, max_overflow=-1)
Session = sessionmaker(bind=engine)


# get weather data by date use sqlalchemy
def get_weather_by_date(start_date,end_date):
    session = Session()
    weather_data = session.query(Weather).filter(Weather.date >= start_date, Weather.date <= end_date).all()
    return weather_data
    


# test get_weather_by_date
if __name__ == "__main__":
    print(get_weather_by_date("2015-1-1","2015-1-5"))
