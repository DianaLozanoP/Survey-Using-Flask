# Survey-Using-Flask
In this exercise, you will build a survey application.  It will ask the site visitor questions from a questionnaire, one per screen, moving to the next question when they submit.
Step Eight: Using the Session
Storing answers in a list on the server has some problems. The biggest one is that there’s only one list – if two people try to answer the survey at the same time, they’ll be stepping on each others’ toes!

A better approach is to use the session to store response information, so that’s what we’d like to do next. If you haven’t learned about the session yet, move on to step 9 and come back to this later.

To begin, modify your start page so that clicking on the button fires off a POST request to a new route that will set session[“responses”] to an empty list. The view function should then redirect you to the start of the survey. (This will also take care of the issue mentioned at the end of Step Six.) Then, modify your code so that you reference the session when you’re trying to edit the list of responses.
