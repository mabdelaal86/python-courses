#!/usr/bin/env python3

'''
To run this example, need to install the following
* pip install flask
* pip install flask_sqlalchemy
* pip install iso8601
'''

from flask import Flask, jsonify, abort, request
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path
from iso8601 import parse_date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{Path(__file__).parent}/school.db'
db = SQLAlchemy(app)


class Student(db.Model):
    __tablename__ = "students"
    sid = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date(), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(50), nullable=True)
    class_num = db.Column('class', db.Integer, nullable=False)
    group = db.Column(db.String(1), nullable=False)

    def __repr__(self):
        return f'<Student ({self.sid}, {self.name})>'

    def to_json(self):
        return {
            "id": self.sid,
            "name": self.name,
            "birth_date": self.birth_date.isoformat(),
            "gender": self.gender,
            "address": self.address,
            "phone": self.phone,
            "class": self.class_num,
            "group": self.group,
        }

    def update_data(self, data):
        self.name = data["name"]
        self.birth_date = parse_date(data["birth_date"])
        self.gender = data["gender"]
        self.address = data["address"]
        self.phone = data["phone"]
        self.class_num = data["class"]
        self.group = data["group"]

    @staticmethod
    def from_json(data):
        student = Student()
        student.sid = data.get("id", None)
        student.update_data(data)
        return student


###############################

@app.route("/students/", methods=['GET'])
def read_all():
    students = Student.query.all()
    return jsonify([s.to_json() for s in students])


@app.route("/students/<int:student_id>", methods=['GET'])
def read(student_id):
    student = Student.query.filter_by(sid=student_id).first()
    if student is None:
        abort(404, "student not found")
    return jsonify(student.to_json())


@app.route("/students/", methods=['POST'])
def create():
    data = request.get_json()
    student = Student.from_json(data)
    db.session.add(student)
    db.session.commit()
    return jsonify(student.to_json()), 201


@app.route("/students/<int:student_id>/", methods=['PUT'])
def update(student_id):
    student = Student.query.filter_by(sid=student_id).first()
    if student is None:
        abort(404, "student not found")
    data = request.get_json()
    student.update_data(data)
    db.session.commit()
    return "", 204


@app.route("/students/<int:student_id>/", methods=['DELETE'])
def delete(student_id):
    student = Student.query.filter_by(sid=student_id).first()
    if student is None:
        abort(404, "student not found")
    db.session.delete(student)
    db.session.commit()
    return "", 204


###############################

@app.errorhandler(400)
@app.errorhandler(404)
@app.errorhandler(405)
def on_error(error):
    return jsonify({"status": error.code, "title": error.description}), error.code


###############################

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
