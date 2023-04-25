from dll.dal import Weather,Population,IndustrialProduction,Finance
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

# get population data by city,sort by year desc
def get_population_by_city(city = 0):
    session = Session()
    population_data = session.query(Population).filter(Population.city == city).order_by(Population.year.asc()).all()
    return population_data

# get all IndustrialProduction ,sort by year asc
def get_industrial_production():
    session = Session()
    industrial_production = session.query(IndustrialProduction).order_by(IndustrialProduction.year.asc()).all()
    return industrial_production

    
# get all finance data,sort by year asc
def get_finance():
    session = Session()
    finance = session.query(Finance).order_by(Finance.year.asc()).all()
    return finance



# test get_weather_by_date
if __name__ == "__main__":
    print(get_weather_by_date("2015-1-1","2015-1-5"))
    print(get_population_by_city(0))