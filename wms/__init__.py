from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app=Flask(__name__)
app.config['SECRET_KEY']='1cb81085f3241bfa'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:root@localhost:5432/WMS'

db= SQLAlchemy(app)
bcrypt=Bcrypt(app)

from wms import routes