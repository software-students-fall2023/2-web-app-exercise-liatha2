from flask import Flask, render_template

app = Flask(__name__)

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

@app.route("/display-gun")
def display_gun():
    return render_template('displayGun.html')