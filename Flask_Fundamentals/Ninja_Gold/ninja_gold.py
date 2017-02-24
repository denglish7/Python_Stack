from flask import Flask, session, render_template, request, redirect
import random
app = Flask(__name__)
app.secret_key = '09f7e02f1290be211da707a266f153b3'



@app.route('/')
def ninjaGold():
    if 'your_gold' not in session:
        session['your_gold'] = 0
    if 'activity_log' not in session:
        session['activity_log'] = []

    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def processMoney():
    building = request.form['building']


    if building == 'farm':
        new_gold = random.randint(10,20)
        session['your_gold'] += new_gold
    elif building == 'casino':
        new_gold = random.randint(-50,50)
        session['your_gold'] += new_gold
    elif building == 'cave':
        new_gold = random.randint(5,10)
        session['your_gold'] += new_gold
    else:
        new_gold = random.randint(2,5)
        session['your_gold'] += new_gold

    new_activity = {
        'activity': "{} {} from the {}".format("Earned" if new_gold > 0 else "Lost", abs(new_gold), building),
        'color': "green" if new_gold > 0 else "red",
    }

    session['activity_log'].append(new_activity)

    print(session['activity_log'])

    return redirect('/')

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

app.run(debug=True)
