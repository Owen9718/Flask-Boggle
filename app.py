from crypt import methods
from boggle import Boggle
from flask import Flask,request,render_template,session,jsonify

app = Flask(__name__)
app.config["SECRET_KEY"] = "fdfgkjtjkkg45yfdb"

boggle_game = Boggle()




@app.route("/")
def board():
    board = boggle_game.make_board()
    session['board'] = board
    return render_template("home.html", board = board)

@app.route("/check_word")
def check():
    word = request.args['guess']
    board = session['board']
    valid = boggle_game.check_valid_word(board,word)
    print(valid)
    return jsonify({"response": valid})