from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField("Enter your username", validators=[DataRequired(), Length(min=6, max=16)])
    password = PasswordField("Enter your password", validators=[DataRequired()])
    submit = SubmitField("Login")
