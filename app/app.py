from flask import Flask
from flask_migrate import Migrate

from models import db
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///abode.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)


@app.route("/")
def abode():
    return "<h1>Welcome to Abode database</h1>"
