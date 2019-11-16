#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask('example_3')


@app.route('/')
@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/welcome")
def welcome():
    user = "Hamdy"
    return render_template('welcome.html', user_name=user)


@app.route("/welcome-dict")
def welcome_dict():
    user = {"name": "Fatma", "age": 23, "gender": "Female"}
    return render_template('welcome-dict.html', user=user)


@app.route("/welcome-list")
def welcome_list():
    students = ["Ahmad", "Samy", "Yasser", "Hoda"]
    return render_template('welcome-list.html', names=students)


app.run(debug=True)
