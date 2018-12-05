from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from app.models.models import User, Businesses, Review
from datetime import date

#register form
class RegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(),Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')


    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('This username is already taken please use a different username')

    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('This email is already taken please use different one')

#login formself
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')


#businesses form
class BusinessesForm(FlaskForm):
    name = StringField('Business name', validators = [DataRequired()])
    location = StringField('Location', validators = [DataRequired()])
    date = DateField('Start date', default = date.today(), format = '%d/%m/%Y',
            validators = [DataRequired(message = 'You need to enter the start date')])
    business_description = TextAreaField('Give the discription of your business')
    submit = SubmitField('Submit')


#review form
class ReviewForm(FlaskForm):
    review_headline = StringField('Review Headline', validators = [DataRequired()])
    comment = TextAreaField('Comment', validators = [DataRequired()])
    submit = SubmitField('Leave a Comment')

#search form
class SearchForm(FlaskForm):
    location = StringField(validators = [DataRequired()])
    submit =SubmitField()