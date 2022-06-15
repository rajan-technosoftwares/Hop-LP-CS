from flask import Blueprint
from flask import request,render_template
from api import db
from api.contact.models import Contact


contact_api=Blueprint('contact_api',__name__,url_prefix='/')

@contact_api.route('/contact-us', methods=['GET','POST'])
def contact():

    if request.method=='POST':
        
        data=request.form
        

        entry=Contact(name=data['name'],email=data['email'],address=data['address'],phone_num=data['phone_num'])
        db.session.add(entry)
        db.session.commit()

    
    return "contact form submitted"

# @contact_api.route('/show_data')
# def show_data():
    
#     data= db.session.query(Contact).all()
#     d=[]
#     for i in data:
#         d.append({
#             'name': i.name,
#             'email': i.email,
#             'address': i.address,
#             'phone_num': i.phone_num,
#         })
#     return {'data': d}


# @contact_api.route('update_data')
# def update_data():
#     data = Contact.query.filter_by(id=7).one()
    
#     if data :
#         data.name='Ravi'
#         db.session.add(data)
#         db.session.commit()

    
    
#     return {'message': 'updated'}

# @contact_api.route('/delete',methods=['POST','GET'])
# def delete():
#     if request.method== 'POST':
#         id_number=request.form.get('id')
#         data= Contact.query.filter(Contact.id==id_number).one()
#         db.session.delete(data)
#         db.session.commit()
#     return render_template('del.html')
