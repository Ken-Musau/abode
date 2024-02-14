import random

from faker import Faker

from app import app
from models import db, Estate, House


fake = Faker()

with app.app_context():

    Estate.query.delete()
    House.query.delete()

    estates = []
    houses = []
    for i in range(10):

        estate = Estate(
            name=fake.name(),
            location=fake.city(),
            price=random.randint(50, 500)
        )
        estates.append(estate)

    db.session.add_all(estates)
    db.session.commit()

    for i in range(10):
        house = House(

            tenant=fake.name(),
            num_of_rooms=random.randint(1, 6),
            price=random.randint(50, 500),
            estate_id=random.randint(1, 10)
        )

        houses.append(house)

    db.session.add_all(houses)
    db.session.commit()
