from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    release_date = Column(Date, nullable=False)
    description = Column(String, nullable=False)
    developer = Column(String, nullable=False)
    image = Column(String, nullable=False)

def create_db_engine(db_url='sqlite:///games.db'):
    return create_engine(db_url)

def create_database():
    engine = create_db_engine()
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    create_database() 

