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
    filter_students = [s for s in students if search_word in s['name'].lower()]
    message = "No students match this name" if len(filter_students) == 0 else ""
    return render_template('search.html', students=filter_students, message=message)


@app.route("/details")
def details():
    id = int(request.args.get('id', ''))
    filter_students = [s for s in students if id == s['id']]
    message = "No student with this id" if len(filter_students) == 0 else ""
    return render_template('details.html', students=filter_students, message=message)


@app.route("/student/<int:id>")
def student(id):
    filter_students = [s for s in students if id == s['id']]
    message = "No student with this id" if len(filter_students) == 0 else ""
    return render_template('details.html', students=filter_students, message=message)


@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        students.append(request.form)
        return render_template('details.html', students=[request.form])
    else:
        return render_template('register.html')


app.run(debug=True)
