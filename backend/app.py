from flask import Flask
from flask_mail import Mail,  Message
from flask_cors import CORS
from flask import request

app = Flask(__name__, "/../frontend/build")

app.config['MAIL_SERVER'] = 'smtp.mail.yahoo.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'rizwankassamali@yahoo.ca'
app.config['MAIL_PASSWORD'] = '786National@3471'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)
CORS(app)


@app.route('/submit/')
def submit():

    # recv data from api
    name = request.args.get('name')
    email = request.args.get('email')
    fsc = request.args.get('sc')
    teamSize = request.args.get('team')
    print(name)
    print(email)
    print(fsc)
    print(teamSize)
    
    # send info to slack

    # send email to the person
    msg = Message('Hello from the other side!', sender='peter@mailtrap.io',
                  recipients=['rizwankassamali1@gmail.com'])
    msg.body = "Hey Paul, sending you this email from my Flask app, lmk if it works"
    mail.send(msg)
    
    return {'hello': 'wofgdfgrld'}
