#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, url_for, make_response
from dotenv import load_dotenv
import os

import pymongo
import datetime
from bson.objectid import ObjectId
import sys
from werkzeug.utils import secure_filename


# instantiate the app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static/upload'

# load credentials and configuration options from .env file
# if you do not yet have a file named .env, make one based on the template in env.example
load_dotenv()  # take environment variables from .env.

# turn on debugging if in development mode
if os.getenv('FLASK_ENV', 'development') == 'development':
    # turn on debugging, if in development
    app.debug = True # debug mnode

# connect to the database
cxn = pymongo.MongoClient(os.getenv('MONGO_URI'), serverSelectionTimeoutMS=5000)
try:
    # verify the connection works by pinging the database
    cxn.admin.command('ping') # The ping command is cheap and does not require auth.
    db = cxn[os.getenv('MONGO_DBNAME')] # store a reference to the database
    print(' *', 'Connected to MongoDB!') # if we get here, the connection worked!
except Exception as e:
    # the ping command failed, so the connection is not available.
    print(' *', "Failed to connect to MongoDB at", os.getenv('MONGO_URI'))
    print('Database connection error:', e) # debug


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/add-gun")
def add_gun():
    return render_template('addGun.html')

@app.route("/delete-gun")
def delete_gun():
    return render_template('deleteGun.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/edit-gun")
def edit_gun():
    return render_template('editGun.html')

@app.route("/display-gun<gun_name>")
def display_gun(gun_name):
    # Fetch the document from MongoDB using its _id
    document = db.guns.find_one({"gun-name": gun_name})
    filename = document.image
    return render_template('displayGun.html', document=document, filename=filename)

@app.route("/search")
def search():
    return render_template('search.html')

@app.route("/submit-gun", methods=["POST"])
def submit_gun():
    gun_image = request.files["gun-image"]
    filename = secure_filename(gun_image.filename)
    gun_image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    gun_name = request.form["gun-name"]
    gun_description = request.form["gun-description"]
    gun_price = request.form["gun-price"]
    
    gun = {
        "image": filename,
        "name": gun_name,
        "description": gun_description,
        "price": float(gun_price)
    }
    
    db.guns.insert_one(gun)
    
    return redirect(url_for("home"))


@app.route("/edit-gun", methods=["POST"])
def editgun():
    gun_image = request.files["gun-image"]
    filename = secure_filename(gun_image.filename)
    gun_image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    gun_description = request.form["gun-description"]
    gun_price = request.form["gun-price"]

    # Assuming you want to update a document based on a unique identifier, for example, the gun name
    gun_name = request.form["gun-name"]
    
    # Define the filter criteria to match the specific document you want to update
    filter_criteria = {"name": gun_name}

    # Define the update operation to update all fields in the matching document
    update_operation = {
        "$set": {
            "name": gun_name,
            "image": filename,
            "description": gun_description,
            "price": float(gun_price)
        }
    }

    try:
        result = db.guns.update_one(filter_criteria, update_operation)
        if result.matched_count == 0:
            # Handle the case where no document matched the criteria
            # You can show an error message or take other appropriate actions
            print("Entry doesn't exist")
    except UpdateError as e:
        # Handle the error if there's an issue with the update
        print("Update failure")

    # Redirect the user to the home page
    return redirect(url_for("home"))
