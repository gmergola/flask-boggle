from boggle import Boggle
from flask import Flask, request, render_template, session, flash
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

boggle_game = Boggle()

BOARD_KEY = 'board'
GUESSES_KEY = 'guesses'


@app.route('/')
def adding_board():
    """adding board to home page"""

    the_board = boggle_game.make_board()
    session[BOARD_KEY] = the_board
    the_board = session[BOARD_KEY]
    session[GUESSES_KEY] = []

    return render_template(
        'board.html',
        board=the_board
                        )

@app.route('/', methods=['POST'])
def guess_form():
    user_guess = request.form.get('guess')

    guess = session[GUESSES_KEY]
    guess.append(user_guess)
    
    


