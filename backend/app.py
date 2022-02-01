from flask import Flask
from flask_mail import Mail,  Message
from flask_cors import CORS
from flask import request
from slack_bolt import App

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
    
    if (str(name) != "None"):
        print(name)
        print(email)
        print(fsc)
        print(teamSize)
        
        # send info to slack
            # https://api.slack.com/messaging/sending
            # cant do slack API, becuase I need a workspace for the hook.
    
        # send email to the person
        msg = Message('Thank you for your interest', sender=email,
                    recipients=['rizwankassamali1@gmail.com'])
        msg.body = "Hi, Thank you for your interest in CodeBox."
        mail.send(msg)
    
    return {'hello': 'TestBox'}
