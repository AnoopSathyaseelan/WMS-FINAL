from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length , Email, EqualTo



   


class Registrationform(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])
    Address=StringField('Address',validators=[DataRequired(), Length(min=20, max=300)])
    Mob_no =  StringField('Mob no',validators=[DataRequired(),])

    submit= SubmitField('Sign Up')


class loginform(FlaskForm):
    
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit= SubmitField('Login')    