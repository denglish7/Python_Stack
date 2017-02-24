from flask import Flask, render_template, flash, redirect, request, session
import re

app = Flask(__name__)
app.secret_key = 'fifeepItSecretKeepItSafe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja', methods=["POST"])
def process():
    tmnt = True
    return render_template("index2.html", tmnt=tmnt)

@app.route('/ninja/<color>')
def color(color):
    tmnt = False
    return render_template("index2.html", color=color, tmnt=tmnt)

app.run(debug=True)
