#!/usr/bin/env python3

from flask import Flask, request, render_template, redirect, url_for

app = Flask('example_7')

students = [
    {"id": 105, "name": "Ibrahim Fatti", "gender": "Male", "birth_date": "1995-12-13", "address": "Giza", "class": 3, "group": "A"},
    {"id": 109, "name": "Shady Hamdy", "gender": "Male", "birth_date": "1995-10-22", "address": "Giza", "class": 3, "group": "B"},
    {"id": 115, "name": "Amani Fahmy", "gender": "Female", "birth_date": "1996-05-12", "address": "Cairo", "class": 2, "group": "A"},
    {"id": 122, "name": "Kareem Ahmad", "gender": "Male", "birth_date": "1997-09-14", "address": "Cairo", "class": 1, "group": "C"}
]


@app.route("/search/")
def search():
    search_word = request.args.get('name', '').lower()
    filter_students = [s for s in students if search_word in s['name'].lower()]
    return render_template('search.html', students=filter_students)


@app.route("/student/<int:student_id>/")
def student(student_id):
    student = next( (s for s in students if student_id == int(s['id']) ), None)
    return render_template('details.html', student=student)


@app.route("/register/", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        students.append(request.form)
        return redirect(url_for('student', student_id=request.form['id']))
    else:
        return render_template('register.html')


app.run(debug=True)
