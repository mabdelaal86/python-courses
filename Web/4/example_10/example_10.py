#!/usr/bin/env python3

from flask import Flask, request, jsonify

print(__name__)
app = Flask(__name__)


students = {
    105: {"id": 105, "name": "Ibrahim Fatti", "gender": "Male", "birth_date": "1995-12-13", "address": "Giza", "class": 3, "group": "A"},
    109: {"id": 109, "name": "Shady Hamdy", "gender": "Male", "birth_date": "1995-10-22", "address": "Giza", "class": 3, "group": "B"},
    115: {"id": 115, "name": "Amani Fahmy", "gender": "Female", "birth_date": "1996-05-12", "address": "Cairo", "class": 2, "group": "A"},
    122: {"id": 122, "name": "Kareem Ahmad", "gender": "Male", "birth_date": "1997-09-14", "address": "Cairo", "class": 1, "group": "C"}
}


@app.route("/students/", methods=['GET'])
def read_all():
    return jsonify(list(students.values()))


@app.route("/students/<int:student_id>/", methods=['GET'])
def read(student_id):
    student = students.get(student_id)
    return jsonify(student)


@app.route("/students/", methods=['POST'])
def create():
    data = request.get_json()
    student_id = data['id']
    if student_id in students:
        return jsonify({"message": "error. duplicated ID"})
    students[student_id] = data
    return jsonify({"message": "success"})


@app.route("/students/<int:student_id>/", methods=['PUT'])
def update(student_id):
    data = request.get_json()
    student = students.get(student_id)

    if student == None:
        return jsonify({"message": "not found"})

    for key in data:
        student[key] = data[key]

    return jsonify({"message": "success"})


@app.route("/students/<int:student_id>/", methods=['DELETE'])
def delete(student_id):
    if student_id not in students:
        return jsonify({"message": "not found"})

    del students[student_id]
    return jsonify({"message": "success"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
