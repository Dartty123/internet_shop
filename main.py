import os

from flask import Flask

from src.database.models import db


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_URI")
db.init_app(app)


#with app.app_context():
#  db.create_all()