import random
from flask import Flask, render_template
from webcolors.constants import CSS3_NAMES_TO_HEX


app = Flask(__name__)



def choose_colour():
    return random.choice(list(CSS3_NAMES_TO_HEX))


@app.route("/")
def home():    
    return render_template('home.html', colour=choose_colour())


@app.route("/partials/change-colour")
def dot():
    return render_template('partials/dot.html', colour=choose_colour())
