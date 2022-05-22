from flask import Flask, render_template,request,render_template
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.secret_key= 'super-secret-key'
app.config["SQLALCHEMY_DATABASE_URI"]="mysql://root:@localhost/contacts"
db=SQLAlchemy(app)



class Contacts(db.Model):

    id=db.Column(db.Integer,nullable=False ,primary_key=True)
    name=db.Column(db.String(50))
    email=db.Column(db.String(50))
    address=db.Column(db.String(100))
    phone_num=db.Column(db.Integer)

@app.route('/contact',methods=['GET','POST'])
def contact():

    name=request.form.get('name')
    email=request.form.get('email')
    address=request.form.get('address')
    phone_num=request.form.get('phone_num')
    print(name,email,address,phone_num)

    entry=Contacts(name=name,email=email,address=address,phone_num=phone_num)
    db.session.add(entry)
    db.session.commit()

    return render_template('add copy.html')

if __name__ == '__main__':
    app.run(debug=True)