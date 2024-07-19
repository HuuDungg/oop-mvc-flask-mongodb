from flask import Flask, render_template, redirect, url_for, flash

from LoginForm import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('login.html', form=form)

@app.route('/home')
def home():
    return 'Home Page'

if __name__ == '__main__':
    app.run(debug=True)
