from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'fifeepItSecretKeepItSafe'
mysql = MySQLConnector(app,'mydb')

@app.route('/')
def index():
    query = "SELECT * FROM email"
    emails = mysql.query_db(query)
    # passing the query into the the query_db function
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if not EMAIL_REGEX.match(request.form['email_address']):
        flash("Invalid email address")

    return redirect('/')

app.run(debug=True)
