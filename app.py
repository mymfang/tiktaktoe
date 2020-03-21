from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session
from tempfile import mkdtemp

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    if "board" not in session:
        session['board'] = [[None, None, None], [None, None, None], [None, None, None]]
        session["turn"] = "X"
    
    return render_template("game.html", game=session["board"], turn=session["turn"])

@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    return redirect(url_for("index"))


@app.route("/button")
def button():
    return render_template("button.html")

@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

@app.route("/exchange")
def exchange():
    return render_template("exchange.html")

@app.route("/react")
def react():
    return render_template("react.html")

@app.route("/addition")
def addition():
    return render_template("addition.html")