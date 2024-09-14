"""
Author      : Shubham Ahinave
Created at  : 02/09/24
"""
import os

from flask import Flask, redirect, url_for
from flask_mail import Mail


mail = None

def create_app(test_config=None):

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('app.core.config.Config')

    global mail
    mail = Mail()
    mail.init_app(app)

    from . import bg_remove
    app.register_blueprint(blueprint=bg_remove.bp)
    # app.add_url_rule('/bg_remove', endpoint='index')

    @app.route('/')
    def hello():
        return redirect(url_for('bg_remove.index'))

    return app
