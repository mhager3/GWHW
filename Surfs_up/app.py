# dependencies
import pandas as pd
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from flask import Flask, jsonify

# set up flask
app = Flask(__name__)

# create the engine
engine = create_engine("sqlite:///db/hawaii_db.sqlite", echo = False)

# Establish the Base
Base = automap_base()

# reflect using the Base class
Base.prepare(engine, reflect=True)

# variables referencing the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# create a session
session = Session(bind=engine)

@app.route("/")
def index():
    return (
        f'Available routes:</br>'
        f'/api/v1.0/precipitation</br>'
        f'/api/v1.0/stations</br>'
        f'/api/v1.0/tobs</br>'
        f'/api/v1.0/date and /api/v1.0/start_date/end_date'
    )

@app.route("/api/v1.0/precipitation")
def precipitation():

    # get date ranges
    last_day = session.query(Measurement.date)\
                    .order_by(Measurement.date.desc()).first()[0]
    first_day = last_day - dt.timedelta(days=364)

    # get precipitation data within the ranges
    year_prcp = session.query(Measurement.date, func.sum(Measurement.prcp))\
                    .filter(Measurement.date >= first_day)\
                    .group_by(Measurement.date)\
                    .order_by(Measurement.date).all()

    data_dict = {}
    for item in year_prcp:
        data_dict[item[0]] = item[1]

    return jsonify(data_dict)

@app.route("/api/v1.0/stations")
def stations():
    # query all stations
    stations = session.query(Station.station).all()

    # convert list of tuples into normal list
    stations_list = list(np.ravel(stations))

    return jsonify(stations_list)

@app.route('/api/v1.0/tobs')
def tobs():

    # get dates for range
    last_day = session.query(Measurement.date)\
                    .order_by(Measurement.date.desc()).first()[0]
    first_day = last_day - dt.timedelta(days=364)

    #get temp data for range 
    year_tobs = session.query(Measurement.date, Measurement.tobs)\
                    .filter(Measurement.date > first_day ).all()

    # convert list of tuples into normal list
    tobs_list = list(np.ravel(year_tobs))

    return jsonify(tobs_list)

@app.route("/api/v1.0/<start_date>")
@app.route("/api/v1.0/<start_date>/<end_date>")
def temp(start_date, end_date=0):

    # if no end_date is provided, use the last day of the data
    if end_date == 0:
        end_date = session.query(Measurement.date)\
                    .order_by(Measurement.date.desc()).first()[0]

    # calculate Min, Avg, and Max for date range    
    temps = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs))\
                .filter(Measurement.date >= start_date)\
                .filter(Measurement.date <= end_date).all()
    
    # convert list of tuples into normal list
    temps_list = list(np.ravel(temps))

    return jsonify(temps_list)

# run the app
if __name__ == "__main__":
    app.run(debug=True)