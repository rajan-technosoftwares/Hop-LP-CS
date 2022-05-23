from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db=SQLAlchemy()

db_name= 'contacts.db'


def create_app():
    app=Flask(__name__)
    
    app.config['SECRET_KEY']='sdcoea,dnpsfipmae9ajfsdfsda.an23rds'
    
    app.config['SQLALCHEMY_DATABASE_URI']= f'sqlite:///{db_name}'
    
    db.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all()
    

    from api.contact.routes import contact_api
    app.register_blueprint(contact_api)



    

    return (app)






