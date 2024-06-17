from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class MyForm(FlaskForm):
    name = StringField(label='Email', validators=[Email(message="Invalid Email")])
    password = PasswordField(label='Password', validators=[Length(min=8, message="Password to be min 8 characters long")])
    submit = SubmitField(label='Log In')
