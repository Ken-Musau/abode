from flask import Flask, jsonify, make_response, request
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


@app.route("/estates", methods=["GET", "POST"])
def estates():
    if request.method == "GET":
        estates = [estate.to_dict() for estate in Estate.query.all()]
        return make_response(estates, 200)

    elif request.method == "POST":
        new_estate = Estate(
            name=request.form.get("name"),
            location=request.form.get("location"),
            price=request.form.get("price")
        )
        db.session.add(new_estate)
        db.session.commit()

        estate_dict = new_estate.to_dict()

        return make_response(jsonify(estate_dict), 201)


@app.route("/estates/<int:id>", methods=["GET", "PATCH", "DELETE"])
def estate_by_id(id):

    estate = Estate.query.filter(Estate.id == id).first()

    if request.method == "GET":
        estate_dict = estate.to_dict()
        return make_response(jsonify(estate_dict), 200)

    elif request.method == "PATCH":
        for attr in request.form:
            setattr(estate, attr, request.form.get(attr))
            db.session.add(estate)
            db.session.commit()

            estate_dict = estate.to_dict()

            return make_response(jsonify(estate_dict), 200)

    elif request.method == "DELETE":
        db.session.delete(estate)
        db.session.commit()

        return make_response({
            "delete Sucessfull": True,
            "Message": "Estate Deleted"
        }, 200)


if __name__ == "__main__":
    app.run(port=5555, debug=True)
