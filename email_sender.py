from flask_mail import Message
from api import app, mail
from flask import render_template


def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template, **kwargs)
    msg.html = render_template(template, **kwargs)
    mail.send(msg)
