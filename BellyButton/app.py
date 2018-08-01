import numpy as np
from flask import Flask, jsonify, render_template

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

# set up flask
app = Flask(__name__)

# create the engine
engine = create_engine("sqlite:///DB/belly_button_biodiversity.sqlite")

# Establish the Base
Base = automap_base()

# reflect using the Base class
Base.prepare(engine, reflect=True)

# create a session
session = Session(bind=engine)


# render the index html
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/names')
def names():

    # setup empty list to capture names
    list = []


    return jsonify(list)


if __name__ == "__main__":
    app.run(debug=True)
