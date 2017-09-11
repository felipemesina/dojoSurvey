from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "speakfriendandenter"


@app.route("/")
def index():
    return render_template("dojosurvey.html")

@app.route("/results", methods=['POST'])
def process_form():
    print "Submit Form Info"
    print request.form
    return render_template("results.html", name = request.form['name'], comment=request.form['comment'], city=request.form['city'], language=request.form['language'])


app.run(debug=True)
