from flask import Blueprint
from flask import request,render_template
from api import db
from api.contact.models import Contacts


contact_api=Blueprint('contact_api',__name__,url_prefix='/')

@contact_api.route('/contact-us', methods=['GET','POST'])
def contact():

    if request.method=='POST':
        name=request.form.get('name')
        email=request.form.get('email')
        address=request.form.get('address')
        phone_num=request.form.get('phone_num')
        # print(name,email,address,phone_num)

        entry=Contacts(name=name,email=email,address=address,phone_num=phone_num)
        db.session.add(entry)
        db.session.commit()

    return render_template('add copy.html')