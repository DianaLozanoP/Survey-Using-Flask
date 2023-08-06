from flask import Flask, request, render_template, redirect, flash
from surveys import satisfaction_survey
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "Checoisstrong"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

responses = []


@app.route("/")
def homepage():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template("startsurvey.html", title=title, instructions=instructions)


@app.route("/questions/<numb>", methods=['GET', 'POST'])
def currentquestion(numb):
    eachnumb = int(numb)
    if (len(responses) == len(satisfaction_survey.questions)):
        return render_template("thankyou.html")
    elif (eachnumb > len(responses)):
        count = len(responses)
        flash("You missed some questions of our valuable survey. Redirecting you.")
        return redirect("/questions/" + str(count))
    else:
        question = satisfaction_survey.questions[eachnumb].question
        choices = satisfaction_survey.questions[eachnumb].choices
        return render_template("questions.html", enumb=eachnumb, question=question, choices=choices)


@app.route("/answer", methods=["GET", "POST"])
def handle_answers():
    answer = request.form["choice"]
    responses.append(answer)
    count = len(responses)
    return redirect("/questions/" + str(count))
