import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DB_SERVER_URL = os.getenv('DB_SERVER_URL')
if DB_SERVER_URL is None:
    raise ValueError("Must provide DB_SERVER_URL")

DB_PORT = os.getenv('DB_PORT')
if DB_PORT is None:
    DB_PORT = 1433

DB_PASSWORD = os.getenv('DB_PASSWORD')
if DB_PASSWORD is None:
    raise ValueError("Must provide DB_PASSWORD")

DB_NAME = os.getenv('DB_NAME')
if DB_NAME is None:
    raise ValueError("Must provide DB_NAME")

DB_USER = os.getenv('DB_USER')
if DB_USER is None:
    raise ValueError("Must provide DB_USER")

SQLALCHEMY_DATABASE_URL = f"mssql+pyodbc://{DB_USER}:{DB_PASSWORD}@{DB_SERVER_URL}:{DB_PORT}/{DB_NAME}?driver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
