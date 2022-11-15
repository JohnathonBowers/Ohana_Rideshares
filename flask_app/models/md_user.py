from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import md_magazine
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# I referred to uibakery.io for how to construct this password regex
PWD_REGEX = re.compile('^(?=.*?[A-Z])(?=.*?[0-9])(?=.*?[!@#$%^&*-?]).{8,20}$')

class User:
    db = 'mag_sub_schema'
    def __init__ (self, db_data:dict):
        self.id = db_data.get('id')
        self.first_name = db_data.get('first_name')
        self.last_name = db_data.get('last_name')
        self.email = db_data.get('email')
        self.password = db_data.get('password')
        self.created_at = db_data.get('created_at')
        self.updated_at = db_data.get('updated_at')
        self.magazines = []
   
    @staticmethod
    def validate_registration(user:dict):
        is_valid = True
        if len(user.get('first_name')) < 1:
            flash('First name must be two or more characters', 'first_name')
            is_valid = False
        if len(user.get('last_name')) < 1:
            flash('Last name must be two or more characters', 'last_name')
            is_valid = False
        if len(user.get('email')) < 1:
            flash('Email address required', 'email')
            is_valid = False
        if not EMAIL_REGEX.match(user.get('email')):
            flash('Please enter a valid email address', 'email')
            is_valid = False
        if not PWD_REGEX.match(user.get('password')):
            flash('Please enter a password that meets the required criteria', 'password')
            is_valid = False
        if (user.get('confirm_password')) != (user.get('password')):
            flash('Passwords do not match!', 'confirm_password')
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(user:dict):
        is_valid = True
        if len(user.get('login_email')) < 1:
            flash('Email address required', 'login_email')
            is_valid = False
        if not EMAIL_REGEX.match(user.get('login_email')):
            flash('Please enter a valid email address', 'login_email')
            is_valid = False
        return is_valid