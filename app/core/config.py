"""
Author      : Shubham Ahinave
Created at  : 15/09/24
"""
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.example.com')
    MAIL_PORT = os.getenv('MAIL_PORT', 587)
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'your_username')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', 'your_password')
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', True)
    MAIL_USE_SSL = os.getenv('MAIL_USE_SSL', False)
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', 'your_email@example.com')
