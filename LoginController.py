from flask import Flask, render_template, redirect, url_for, flash

from LoginForm import LoginForm
from RegisterForm import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

@app.route('/loginForm', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/registerForm', methods=['GET'])
def registerForm():
    return render_template('register.html', form=RegisterForm())
@app.route('/home')
def home():
    return 'Home Page'

if __name__ == '__main__':
    app.run(debug=True)
