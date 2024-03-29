from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username:',validators=[Required()])
    email = StringField('Email:',validators=[Required(), Email()])
    password = PasswordField('Password:',validators=[Required(),EqualTo('password_confirm',message='Password must match')])
    password_confirm = PasswordField('Confirm Password:',validators=[Required()])
    submit = SubmitField('Register')

    def validate_email(self,data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('There is an account with email.')
    
    def validate_username(self,data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('Try another username.')

class LoginForm(FlaskForm):
    email = StringField('Email:',validators=[Required(),Email()])
    password = PasswordField('Password:',validators=[Required()])
    remember = BooleanField('Remember Me:')
    submit = SubmitField('Login')