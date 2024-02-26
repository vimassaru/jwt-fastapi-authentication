from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLCHEMY_DATABASE_URL = 'sqlite:///./todoapp.db'

engine = create_engine(SQLCHEMY_DATABASE_URL, connect_args={
                       'check_same_thread': False})

SessionLocal = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()
