from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db=SQLAlchemy()

db_name= 'contacts.db'
user_name='root'
password =''
host='localhost'

def create_app():
    app=Flask(__name__)
    
    app.config['SECRET_KEY']='sdcoea,dnpsfipmae9ajfsdfsda.an23rds'
    # app.config['SQLALCHEMY_DATABASE_URI']= f"mysql://{user_name}:{password}:@{host}/{Database_name}"
    app.config['SQLALCHEMY_DATABASE_URI']= f'mysql+pymysql://{user_name}{password}:@{host}/{db_name[0:-3]}'
    
    db.init_app(app)
    create_database(app)

    from api.contact.routes import contact_api
    app.register_blueprint(contact_api)



    # create_database(app)

    return (app)

def create_database(app):
    if not path.exists('api/' + db_name):
        db.create_all(app=app)
        print('Created Database!')




