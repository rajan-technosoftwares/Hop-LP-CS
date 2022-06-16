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
    
    
    entry=Contact(name=data['name'],email=data['email'],pin_code=data['pin_code'],phone_num=data['phone_num'])
    db.session.add(entry)
    db.session.commit()
                    
    msg = Message(
            'Contact Details',
            recipients = ['bagoriarajan@gmail.com']
            )
    msg.html =f''' <!DOCTYPE html>
                <html lang="en">
                    <html>
                        <body>
                            <h1 style="margin-top: 0; font-size: 22px;">Contact Details</h1>

                            <table class="table">
                                <tbody>
                                    <tr>
                                        <th scope="row" style="background: #e9e9e9; padding: 8px 10px; text-align: left;">Name</th>
                                        <td style="background: #f5f3f3; padding: 8px 10px; text-align: left;">{ data['name'] }</td>
                                    </tr>
                                    <tr>
                                        <th scope="row" style="background: #e9e9e9; padding: 8px 10px; text-align: left;">Email</th>
                                        <td style="background: #f5f3f3; padding: 8px 10px; text-align: left;">J{ data['email'] }</td>
                                    </tr>
                                    <tr>
                                        <th scope="row" style="background: #e9e9e9; padding: 8px 10px; text-align: left;">Phone Number</th>
                                        <td style="background: #f5f3f3; padding: 8px 10px; text-align: left;">{ data['phone_num'] }</td>
                                    </tr>
                                    <tr>
                                        <th scope="row" style="background: #e9e9e9; padding: 8px 10px; text-align: left;">Pin Code</th>
                                        <td style="background: #f5f3f3; padding: 8px 10px; text-align: left;">{ data['pin_code'] }</td>
                                    </tr>
                                </tbody>
                            </table>
                        </body>
                    </html>
                </html>'''
    
    mail.send(msg)
        
        

    
    return "Contact Form Submitted"
