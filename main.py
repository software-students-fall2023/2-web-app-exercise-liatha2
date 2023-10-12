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