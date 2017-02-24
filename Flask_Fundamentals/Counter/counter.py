from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsMySecret'

def hitCounter():
    try:
        session['counter'] += 1
    except Exception:
        session['counter'] = 1

def plusTwo():
    try:
        session['counter'] += 1
    except Exception:
        pass

@app.route('/', methods=['POST', 'GET'])
def counterPage():
    hitCounter()
    return render_template('counter.html')

@app.route('/reset', methods=['POST', 'GET'])
def resetCounter():
    session.clear()
    return redirect('/')

@app.route('/plusTwo', methods=['POST', 'GET'])
def plusTwoButton():
    plusTwo()
    return redirect('/')

app.run(debug=True)
