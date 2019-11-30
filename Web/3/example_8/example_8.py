#!/usr/bin/env python3

from flask import Flask, request, session, make_response

app = Flask('example_8')


@app.route("/c1")
def c1():
    username = request.cookies.get('username')
    return "User Name: " + username


@app.route("/c2")
def c2():
    resp = make_response("Set Username")
    resp.set_cookie('username', 'Amgad')
    return resp


app.run(debug=True)
