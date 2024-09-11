"""
Author      : Shubham Ahinave
Created at  : 02/09/24
"""
import os

from flask import Flask, redirect, url_for


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(os.path.join(app.instance_path, 'upload_images'))
    except OSError:
        pass

    from . import bg_remove
    app.register_blueprint(blueprint=bg_remove.bp)
    # app.add_url_rule('/bg_remove', endpoint='index')

    @app.route('/')
    def hello():
        return redirect(url_for('bg_remove.index'))

    return app



# https://bootstraptemple.com/p/bootstrap-image-upload