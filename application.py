from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session
from tempfile import mkdtemp

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

BOARD_SIZE = 3

# ****** index
@app.route("/")
def index():
    return "404"

# ****** game tiktactoe
@app.route("/tiktactoe")
def tiktactoe():


    if "board" not in session:

        #多维数组创建,方法1
        '''
        list1 = []
        list2 = []
        for i in range(BOARD_SIZE):
            list1.append(None)
        for j in range(BOARD_SIZE):
            list2.append(list1)
        session["board"] = list2
        '''
        #方法2
        session["board"] = [[None]*BOARD_SIZE for _ in range(BOARD_SIZE)]
        session["turn"] = "X"
    
    return render_template("tiktactoe.html", game=session["board"], turn=session["turn"], size=BOARD_SIZE)

@app.route("/play/<int:row>/<int:col>")
def player(row, col):
    if session["turn"] == "X":
        session["board"][row][col] = "X"
        session["turn"] = "O"
    else:
        session["board"][row][col] = "O"
        session["turn"] = "X"

    pointer = 0
    #counter = 0
    #scores_X = [r0,r1,r2,c0,c1,c2,t0,t1]
    scores_X = [0,0,0,0,0,0,0,0]
    scores_O = [0,0,0,0,0,0,0,0]

    for i in session["board"]:
        for j in range(3):
            if i[j] == "X":
                # 更新row数据
                scores_X[pointer] += 1
                # 更新col数据
                scores_X[j+3] += 1
                # 更新tilt1数据
                if (pointer+1) / (j+1) == 1:
                    scores_X[6] += 1
                # 更新另一个斜面的数据
                if pointer == 2 and j == 0:
                    scores_X[7] += 1
                if pointer == 1 and j == 1:
                    scores_X[7] += 1
                if pointer == 0 and j == 2:
                    scores_X[7] += 1
            elif i[j] == "O":
                scores_O[pointer] += 1
                scores_O[j+3] += 1
                # tilt1
                if ((pointer+1) / (j+1)) == 1:
                    scores_O[6] += 1
                # tilt2
                if pointer == 2 and j == 0:
                    scores_O[7] += 1
                if pointer == 1 and j == 1:
                    scores_O[7] += 1
                if pointer == 0 and j == 2:
                    scores_O[7] += 1
            else:
                continue
        pointer += 1

        if max(scores_X) == 3:
            return render_template("tiktactoe_result.html", winner="X")
        elif max(scores_O) == 3:
            return render_template("tiktactoe_result.html", winner="O")
    
    return redirect(url_for("tiktactoe"))

@app.route("/play/reset")
def new_game():
    session["board"] = [[None]*BOARD_SIZE for _ in range(BOARD_SIZE)]
    session["turn"] = "X"
    return redirect(url_for("tiktactoe"))



# ****** button
@app.route("/button")
def button():
    return render_template("button.html")

# ****** quiz
@app.route("/quiz")
def quiz():
    return render_template("quiz.html")
# ****** exchange
@app.route("/exchange")
def exchange():
    return render_template("exchange.html")

# ****** react
@app.route("/react")
def react():
    return render_template("react.html")

# ****** addition
@app.route("/addition")
def addition():
    return render_template("addition.html")