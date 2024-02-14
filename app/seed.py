from faker import Faker

from app import app
from models import db, Estate, House


fake = Faker()

with app.app_context():

    Estate.query.delete()
    House.query.delete()
    
    estates = []
    for i in range(10):
        
