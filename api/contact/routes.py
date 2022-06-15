from flask import Blueprint, Response
from flask import request,render_template
from api import db
from api.contact.models import Contact
from flask_cors import cross_origin

contact_api=Blueprint('contact_api',__name__,url_prefix='/')

@contact_api.route('/contact-us', methods=['POST'])
@cross_origin()
def contact():

    if request.method=='POST':
        
        data=request.form
        resp = Response("contact form submitted")
        resp.headers['Access-Control-Allow-Origin'] = '*'
        entry=Contact(name=data['name'],email=data['email'],pin_code=data['pin_code'],phone_num=data['phone_num'])
        db.session.add(entry)
        db.session.commit()

    
    return resp
