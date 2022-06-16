from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from flask_mail import Mail
db=SQLAlchemy()
# mail=Mail()
mail=''
db_name= 'contacts.db'


def create_app():
    app=Flask(__name__)
    cors = CORS(app)
    global mail
    mail=Mail(app)
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465

    app.config['MAIL_USERNAME'] = 'rajan.b.technosoftwares@gmail.com'
    app.config['MAIL_PASSWORD'] = 'rajan#123'
    app.config['MAIL_DEFAULT_SENDER'] = 'rajan.b.technosoftwares@gmail.com'

    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    mail.init_app(app)
    
    
    app.config['CORS_HEADERS'] = 'Access-Control-Allow-Origin'
    
    app.config.from_object('config.Config')
    db.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all()
    

    from api.contact.routes import contact_api
    app.register_blueprint(contact_api)



    

    return (app)






