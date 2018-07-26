from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app)

# default route
@app.route('/')
def index():
    data = mongo.db.data.find_one()
    return render_template('index.html', data=data)

# scraping
@app.route('/scrape')
def scraper():
    data = mongo.db.data
    mars_data = scrape_mars.scrape()
    #update the mars db w/ mars_data
    data.update({}, mars_data, upsert=True)
    return index()

#run the app
if __name__ == '__main__':
    app.run(debug=True)