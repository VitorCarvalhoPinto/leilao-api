import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", 'postgresql+psycopg2://postgres:1204@localhost:5432/leilao')
    SQLALCHEMY_TRACK_MODIFICATIONS = False