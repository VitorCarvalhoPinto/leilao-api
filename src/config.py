import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", 'postgresql+psycopg2://user:password@host:port/')
    SQLALCHEMY_TRACK_MODIFICATIONS = False