#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask('example_5')


@app.route('/')
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html', title="About Us")

@app.route("/contact")
def contact():
    return render_template('contact.html', title="Contact Us")


app.run(debug=True)
