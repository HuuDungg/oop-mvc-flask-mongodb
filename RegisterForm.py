from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class RegisterForm(FlaskForm):
    email = StringField("Enter email", validators=[DataRequired(), Length(max=50)])
    username = StringField("Enter username", validators=[DataRequired(), Length(min=6, max=16)])
    password = PasswordField("Enter password", validators=[DataRequired(), Length(min=6)])
    submit  = SubmitField("Submit")