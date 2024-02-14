from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class Estate(db.Model):
    __tablename__ = "estates"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    price = db.Column(db.Integer)

    houses = db.relationship("House", back_populates="estate")

    def __repr__(self):
        return f"{self.name}"


class House(db.Model):
    __tablename__ = "houses"

    id = db.Column(db.Integer, primary_key=True)
    tenant = db.Column(db.String)
    num_of_rooms = db.Column(db.Integer)
    price = db.Column(db.Integer)

    estate_id = db.Column(db.Integer, db.ForeignKey("estates.id"))
