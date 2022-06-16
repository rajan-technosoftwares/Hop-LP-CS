from flask_mail import Message
import json
from pprint import pprint
from flask import Blueprint, Response
from flask import request,render_template
from api import db,mail
from api.contact.models import Contact
from flask_cors import cross_origin

contact_api=Blueprint('contact_api',__name__,url_prefix='/')

@contact_api.route('/contact-us', methods=['GET','POST'])
@cross_origin()
def contact():

    
        
    d=request.get_data()
    data=json.loads(d)
    print(data)
    
    entry=Contact(name=data['name'],email=data['email'],pin_code=data['pin_code'],phone_num=data['phone_num'])
    db.session.add(entry)
    db.session.commit()
                    
    msg = Message(
            'Contact Details',
            recipients = ['bagoriarajan@gmail.com']
            )
    msg.html =f''' <!DOCTYPE html><html lang="en"><html><body>
                    <h1> Contact Details </h1>
                    <table border="1">
                        <tr>
                            <th>Name</th>
                            <th>Email</th>
                            <th>Phone Number</th>
                            <th>Pin Code</th>
                        </tr>
                        <tr>
                            <td>{ data['name'] }</td>
                            <td>{ data['email'] }</td>
                            <td>{ data['phone_num'] }</td>
                            <td>{ data['pin_code'] }</td>

                        </tr>
                        
                    </table>
                    </body>
                    </html>'''
    print(msg)
    mail.send(msg)
        
        

    
    return "Contact Form Submitted"
