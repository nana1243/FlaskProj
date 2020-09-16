
from backend.api.utils.database import db



class products(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    productname = db.Column(db.String(50))
    price = db.Column(db.String(50))
    servicename = db.Column(db.String(50))



