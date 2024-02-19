from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS


from models import db, Estate, House

app = Flask(__name__)
CORS(app)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///abode.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)


class Welcome(Resource):
    def get(self):
        return make_response("<h1>Welcome to Abode database</h1>", 200)


api.add_resource(Welcome, "/")


@app.errorhandler(404)
def handle_not_found(e):

    response = make_response(
        "Not Found: The requested resource does not exist.",
        404
    )

    return response


class Estates(Resource):
    def get(self):
        estates = [estate.to_dict() for estate in Estate.query.all()]

        return make_response(jsonify(estates), 200)

    def post(self):
        data = request.get_json()
        new_estate = Estate(
            name=data.get("name"),
            location=data.get("location"),
            price=data.get("price")
        )

        db.session.add(new_estate)
        db.session.commit()

        return make_response(jsonify(new_estate.to_dict()), 201)


api.add_resource(Estates, "/estates")


class EstateById(Resource):
    def get(self, id):
        estate = Estate.query.filter_by(id=id).first()

        return make_response(jsonify(estate.to_dict()), 200)

    def patch(self, id):
        estate = Estate.query.filter_by(id=id).first()

        data = request.get_json()
        for attr, value in data.items():
            setattr(estate, attr, value)

        db.session.commit()

        return make_response(estate.to_dict(), 200)

    def delete(self, id):
        estate = Estate.query.filter_by(id=id).first()
        db.session.delete(estate)
        db.session.commit()

        return make_response(["Estate deleted"], 200)


api.add_resource(EstateById, "/estates/<int:id>")


class Houses(Resource):
    def get(self):
        houses = [house.to_dict() for house in House.query.all()]
        return make_response(jsonify(houses), 200)

    def post(self):
        data = request.get_json()

        new_house = House(
            tenant=data.get("tenant"),
            num_of_rooms=data.get("num_of_rooms"),
            price=data.get("price"),
            estate_id=data.get("estate_id")
        )

        db.session.add(new_house)
        db.session.commit()

        return make_response(jsonify(new_house.to_dict()), 201)


api.add_resource(Houses, "/houses")


class HouseById(Resource):
    def get(self, id):
        house = House.query.filter_by(id=id).first()

        return make_response(jsonify(house.to_dict()), 200)

    def patch(self, id):
        house = House.query.filter_by(id=id).first()

        data = request.get_json()
        for attr, value in data.items():
            setattr(house, attr, value)

        db.session.commit()

        return make_response(jsonify(house.to_dict()), 200)

    def delete(self, id):
        house = House.query.filter_by(id=id).first()
        db.session.delete(house)

        return make_response("House deleted", 200)


api.add_resource(HouseById, "/houses/<int:id>")

if __name__ == "__main__":
    app.run(port=5555, debug=True)


# @app.route("/")
# def abode():
#     return "<h1>Welcome to Abode database</h1>"


# @app.route("/estates", methods=["GET", "POST"])
# def estates():
#     if request.method == "GET":
#         estates = [estate.to_dict() for estate in Estate.query.all()]
#         return make_response(estates, 200)

#     elif request.method == "POST":
#         new_estate = Estate(
#             name=request.form.get("name"),
#             location=request.form.get("location"),
#             price=request.form.get("price")
#         )
#         db.session.add(new_estate)
#         db.session.commit()

#         estate_dict = new_estate.to_dict()

#         return make_response(jsonify(estate_dict), 201)


# @app.route("/estates/<int:id>", methods=["GET", "PATCH", "DELETE"])
# def estate_by_id(id):

#     estate = Estate.query.filter(Estate.id == id).first()

#     if request.method == "GET":
#         estate_dict = estate.to_dict()
#         return make_response(jsonify(estate_dict), 200)

#     elif request.method == "PATCH":
#         for attr in request.form:
#             setattr(estate, attr, request.form.get(attr))
#             db.session.add(estate)
#             db.session.commit()

#             estate_dict = estate.to_dict()

#             return make_response(jsonify(estate_dict), 200)

#     elif request.method == "DELETE":
#         db.session.delete(estate)
#         db.session.commit()

#         return make_response({
#             "delete Sucessfull": True,
#             "Message": "Estate Deleted"
#         }, 200)


# @app.route("/houses", methods=["GET", "POST"])
# def houses():
#     if request.method == "GET":

#         return make_response(jsonify([estate.to_dict() for estate in Estate.query.all()]), 200)

#     elif request.method == "POST":
#         new_house = House(
#             tenant=request.form.get("tenant"),
#             num_of_rooms=request.form.get("num_of_rooms"),
#             price=request.form.get("price"),
#             estate_id=request.form.get("estate_id")
#         )

#         db.session.add(new_house)
#         db.session.commit()

#         house_dict = new_house.to_dict()
#         return make_response(jsonify(house_dict), 200)


# @app.route("/houses/<int:id>", methods=["GET", "PATCH", "DELETE"])
# def houe_by_id(id):

#     house = House.query.filter_by(id == id).first()

#     if request.method == "GET":
#         house_dict = house.to_dict()
#         return make_response(jsonify(house_dict), 200)

#     elif request.method == "PATCH":
#         for attr in request.form:
#             setattr(house, attr, request.form.get(attr))

#             db.session.add(house)
#             db.session.commit()

#             house_dict = house.to_dict()

#             return make_response(jsonify(house_dict), 200)

#     elif request.method == "DELETE":
#         db.session.delete(house)
#         db.session.commit()

#         return make_response(["House was successfully deleted"])
