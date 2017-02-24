from flask import Flask, render_template, flash, redirect, request, session
import re
from datetime import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'fifeepItSecretKeepItSafe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():

    if len(request.form['email' or 'first_name' or 'last_name' or 'password' or 'confirm_password']) < 1:
        flash("All fields are required!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email address")
    elif not str.isalpha(str(request.form['first_name'])):
        flash("First name cannot contain any numbers or symbols")

    if not request.form['password'] == request.form['confirm_password']:
        flash("Passwords do not match!")
    elif len(request.form['password']) < 8:
        flash("Password must be at least 8 characters long!")
    elif str.islower(str(request.form['password'])):
        flash("Password must contain at least 1 uppercase letter and 1 numeric value.")
    elif not str.isalnum(str(request.form['password'])):
        flash("Password must contain at least 1 uppercase letter and 1 numeric value.")

    if request.form['birthdate'] == '':
        flash('Please pick a birthday')
    else:
        session['birthdate'] = request.form['birthdate']
        now = datetime.now()
        birthDate = datetime.strptime(session['birthdate'], "%Y-%m-%d")

        if now > birthDate:
            pass
        else:
            flash('Birthdate must be in the past')

    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    return redirect('/')

app.run(debug=True)
