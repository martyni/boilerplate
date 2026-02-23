'''Basic flask app'''
from os import environ, path

# config.py


BASE_DIR = path.abspath(path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = (
    "sqlite://" + path.join(BASE_DIR, "app.db")
)

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev-secret-key"
