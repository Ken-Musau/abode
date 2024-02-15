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


@app.route("/houses", methods=["GET", "POST"])
def houses():
    if request.method == "GET":

        return make_response(jsonify([estate.to_dict() for estate in Estate.query.all()]), 200)

    elif request.method == "POST":
        new_house = House(
            tenant=request.form.get("tenant"),
            num_of_rooms=request.form.get("num_of_rooms"),
            price=request.form.get("price"),
            estate_id=request.form.get("estate_id")
        )

        db.session.add(new_house)
        db.session.commit()

        house_dict = new_house.to_dict()
        return make_response(jsonify(house_dict), 200)


@app.route("/houses/<int:id>", methods=["GET", "PATCH", "DELETE"])
def houe_by_id(id):

    house = House.query.filter_by(id == id).first()

    if request.method == "GET":
        house_dict = house.to_dict()
        return make_response(jsonify(house_dict), 200)

    elif request.method == "PATCH":
        for attr in request.form:
            setattr(house, attr, request.form.get(attr))

            db.session.add(house)
            db.session.commit()

            house_dict = house.to_dict()

            return make_response(jsonify(house_dict), 200)

    elif request.method == "DELETE":
        db.session.delete(house)
        db.session.commit()

        return make_response(["House was successfully deleted"])


if __name__ == "__main__":
    app.run(port=5555, debug=True)
