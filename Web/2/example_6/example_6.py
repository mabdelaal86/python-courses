#!/usr/bin/env python3

from flask import Flask, request, render_template

app = Flask('example_6')

students = [
    {"id": 105, "name": "Ibrahim Fatti", "gender": "Male", "birth_date": "1995-12-13", "address": "Giza", "class": 3, "group": "A"},
    {"id": 109, "name": "Shady Hamdy", "gender": "Male", "birth_date": "1995-10-22", "address": "Giza", "class": 3, "group": "B"},
    {"id": 115, "name": "Amani Fahmy", "gender": "Female", "birth_date": "1996-05-12", "address": "Cairo", "class": 2, "group": "A"},
    {"id": 122, "name": "Kareem Ahmad", "gender": "Male", "birth_date": "1997-09-14", "address": "Cairo", "class": 1, "group": "C"}
]


@app.route("/search")
def search():
    search_word = request.args.get('name', '').lower()

    filter_students = []
    for s in students:
        if search_word in s['name'].lower():
            filter_students.append(s)

    return render_template('search.html', students=filter_students)


@app.route("/details")
def details():
    id = int(request.args.get('id', ''))

    student = None
    for s in students:
        if id == s['id']:
            student = s
            break

    return render_template('details.html', student=student)


app.run(debug=True)
