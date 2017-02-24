from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsMySecret'

@app.route('/')
def dojoSurvey():
    return render_template("dojo_survey.html")

@app.route('/result', methods=['POST'])
def surveyResults():
    return render_template("dojo_survey_results.html")

app.run(debug=True)
