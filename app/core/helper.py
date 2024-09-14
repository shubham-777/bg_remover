"""
Author      : Shubham Ahinave
Created at  : 15/09/24
"""
from flask import render_template
from flask_mail import Message

from app import mail


def send_email(to, subject, template_name, template_context):
    try:
        msg = Message(subject=subject, recipients=[to])
        msg.body  = 'Hello'
        # msg.html = render_template(template_name, **template_context)
        mail.send(msg)
    except Exception as e:
        print(e)
        raise e