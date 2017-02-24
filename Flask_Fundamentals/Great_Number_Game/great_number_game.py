from flask import Flask, session, render_template, request, redirect
import random
app = Flask(__name__)
app.secret_key = 'ThisIsMySecret'

@app.route('/')
def greatNumberGame():
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def userGuess():
    if 'rand' not in session:
        session['rand'] = random.randrange(0,101)

    guess = int(request.form['guess'])

    if guess < session['rand']:
        session['guess'] = "tooLow"
    elif guess > session['rand']:
        session['guess'] = "tooHigh"
    else:
        session['guess'] = "correct"

    return redirect('/')

@app.route('/reset', methods=['POST'])
def resetGame():
    session.clear()
    return redirect('/')

app.run(debug=True)
