from api import db




class Contacts(db.Model):

    id=db.Column(db.Integer,nullable=False ,primary_key=True)
    name=db.Column(db.String(50))
    email=db.Column(db.String(50))
    address=db.Column(db.String(100))
    phone_num=db.Column(db.Integer)