from flask import Flask, request, render_template, redirect, flash, session
from surveys import satisfaction_survey
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "Checoisstrong"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

responses = []


@app.route("/")
def homepage():
    # extract the title and the instruction from surveys.py file
    # using satisfaction_survey, which calls Survey class and also Question class
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template("startsurvey.html", title=title, instructions=instructions)


@app.route("/handle-responses", methods=['GET', 'POST'])
def handle_sessions_responses():
    # Set the session responses to an empty list.
    session["responses"] = []
    # Redirect to the start of the survey
    return redirect("/questions/0")


@app.route("/questions/<numb>", methods=['GET', 'POST'])
def currentquestion(numb):
    eachnumb = int(numb)
    count = len(session["responses"])
    # check if all the answers have been answered to thank the customer
    if (count == len(satisfaction_survey.questions)):
        return render_template("thankyou.html")
    # check if the number of the question is lower than the number of answers provided by customer
    # if number is lower, redirect them to the the appropiate question based on the answers provided
    elif (eachnumb > count):
        flash("You missed some questions of our valuable survey. Redirecting you.")
        return redirect("/questions/" + str(count))
    # create question and choices based on the index number
    else:
        question = satisfaction_survey.questions[eachnumb].question
        choices = satisfaction_survey.questions[eachnumb].choices
        return render_template("questions.html", enumb=eachnumb, question=question, choices=choices)


@app.route("/answer", methods=["GET", "POST"])
def handle_answers():
    # get the answer from each question
    answer = request.form["choice"]
    # append the answer to session["responses"]
    responses = session["responses"]
    responses.append(answer)
    session["responses"] = responses
    # Check the number of answers in the responses list
    # Based on that provide the next number for the next question
    count = len(session["responses"])
    return redirect("/questions/" + str(count))
