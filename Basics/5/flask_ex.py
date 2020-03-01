#!/usr/bin/env python3

from flask import Flask

app = Flask('my_app')


@app.route('/')
def index():
    return "Hello, Welcome in Resala Foundation."


app.run()
