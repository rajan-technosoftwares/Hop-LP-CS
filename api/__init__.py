from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

db_name= 'contacts.db'


def create_app():
    app=Flask(__name__)
    
    app.config.from_object('config.Config')
    db.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all()
    

    from api.contact.routes import contact_api
    app.register_blueprint(contact_api)



    

    return (app)






