from flask import Flask, jsonify, make_response
from flask_migrate import Migrate

from models import db, Estate, House

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///abode.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route("/")
def abode():
    return "<h1>Welcome to Abode database</h1>"


@app.route("/estates")
def estates():
    estates = [estate for estate in Estate.query.all()]

    return make_response(jsonify(estates), 200)


if __name__ == "__main__":
    app.run(port=5555, debug=True)
