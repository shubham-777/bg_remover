"""
Author      : Shubham Ahinave
Created at  : 12/09/24
"""
from app import create_app

if __name__ == '__main__':
    create_app = create_app()
    create_app.run(host='0.0.0.0')
else:
    gunicorn_app = create_app()