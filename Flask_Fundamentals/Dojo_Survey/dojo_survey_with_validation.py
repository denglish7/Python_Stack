from flask import Flask, render_template, flash, redirect, request, session
app = Flask(__name__)
app.secret_key = 'epItSecretKeepItSafe'


@app.route('/')
def index():
    return render_template('dojo_survey.html')

@app.route('/process', methods=['POST'])
def process():
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
    else:
        flash("Success! Your name is {}".format(request.form['name']))

    if len(request.form['comments']) > 120:
        flash("Too many characters! Please limit your comments to 120 characters")
    return render_template("dojo_survey_results.html")

@app.route('/reset')
def reset():
    return redirect("/")

app.run(debug=True)
