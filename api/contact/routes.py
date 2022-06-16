from flask_mail import Message
import json
from pprint import pprint
from flask import Blueprint, Response
from flask import request,render_template
from api import db,mail
from api.contact.models import Contact
from flask_cors import cross_origin

contact_api=Blueprint('contact_api',__name__,url_prefix='/')

@contact_api.route('/contact-us', methods=['POST'])
@cross_origin()
def contact():

    if request.method=='POST':
        
        d=request.get_data()
        data=json.loads(d)
        print(data)
        # resp = Response("Contact Form Submitted")
        # resp.headers['Access-Control-Allow-Origin'] = '*'
        entry=Contact(name=data['name'],email=data['email'],pin_code=data['pin_code'],phone_num=data['phone_num'])
        db.session.add(entry)
        db.session.commit()
                     
        msg = Message(
                'Contact Details',
                recipients = ['bagoriarajan@gmail.com']
               )
        msg.body = json.dumps(data)
        print(mail.send(msg))
        
        

    
    return "Contact Form Submitted"
