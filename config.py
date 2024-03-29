import os

basedir = os.path.abspath(os.path.dirname(__file__))  # место, где будет храниться файл БД


class Config:
    SECRET_KEY = "SECRET_KEY"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
