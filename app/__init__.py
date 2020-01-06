from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

#Database Config
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#Scheduler
from app.models import Data
from datetime import datetime
from time import time
from random import random
import atexit
from Sensor/Temp_function import t

scheduler = BackgroundScheduler()

#writing Data
def write():
    db.session.rollback()
    d = Data(date = time(), temp = t())
    db.session.add(d)
    db.session.commit()


scheduler.add_job(func=write, trigger="interval", seconds = 5)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())

from app import routes, models
