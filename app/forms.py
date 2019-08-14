from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import Users


class PostForm(FlaskForm):

    title = StringField('Title',
                            validators=[
                                DataRequired(),
                                Length(min=4, max=100)
                            ])

    content = StringField('Content',
                        validators=[
                            DataRequired(),
                            Length(min=50, max=10000)
                        ])

    submit = SubmitField('Post Content')


class RegistrationForm(FlaskForm):


    first_name = StringField('First Name',
                             validators=[
                                 DataRequired(),
                                 Length(min=2, max=30)
                             ])

    last_name = StringField('Last Name',
                            validators=[
                                DataRequired(),
                                Length(min=2, max=30)
                            ])

    email = StringField('Email',
                        validators=[
                            DataRequired(),
                            Email(),
                        ])

    password = PasswordField('Password',
                        validators=[
                            DataRequired(),
                            Length(min=8, max=30),
                        ])
    confirm_password = PasswordField('Confirm Password',
                             validators=[
                                 DataRequired(),
                                 EqualTo('password'),
                             ])

    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already in use!')