from flask import Flask, render_template, redirect, url_for #flask to render a template, redirect, and create url
from flask_pymongo import PyMongo #pymongo will be used to interact with our mongo db  (mars_app)
import scraping # scraping code to convert from Jupyter to Python

app = Flask(__name__) #set up Flask

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# set up app routes using flask protocol
@app.route("/") #home page
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

@app.route("/scrape") #scrape button of the web app to update on demand
def scrape(): 
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)

.update(query_parameter, data, options)
return redirect('/', code=302) #success code
if __name__ == "__main__":
   app.run()