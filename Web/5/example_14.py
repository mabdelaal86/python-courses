#!/usr/bin/env python3

from flask import Flask, request, jsonify, abort
import sqlite3
from pathlib import Path

db_file = str(Path(__file__).parent) + "/school.db"


app = Flask(__name__)


@app.route("/students/", methods=['GET'])
def read_all():
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")

    rows = cur.fetchall()
    students = [read_student(row) for row in rows]
    conn.close()

    return jsonify(students)


@app.route("/students/<int:student_id>/", methods=['GET'])
def read(student_id):
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE id=?", (student_id,))

    row = cur.fetchone()
    if row is None:
        conn.close()
        abort(404, "Student not found")

    student = read_student(row)
    conn.close()

    return jsonify(student)


@app.route("/students/", methods=['POST'])
def create():
    data = request.get_json()
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    sql = "INSERT INTO students VALUES(null,:name,:birth_date,:gender,:address,:phone,:class,:group)"
    cur.execute(sql, data)
    data['id'] = cur.lastrowid
    conn.commit()
    conn.close()

    return jsonify(data), 201


@app.route("/students/<int:student_id>/", methods=['PUT'])
def update(student_id):
    data = request.get_json()
    data['id'] = student_id

    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    sql = 'UPDATE students SET "name"=:name, "birth_date"=:birth_date, "gender"=:gender, "address"=:address, "phone"=:phone, "class"=:class, "group"=:group WHERE "id"=:id'

    cur.execute(sql, data)
    if cur.rowcount == 0:
        conn.close()
        abort(404, "Student not found")

    conn.commit()
    conn.close()
    
    return "", 204


@app.route("/students/<int:student_id>/", methods=['DELETE'])
def delete(student_id):
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    sql = "DELETE FROM students WHERE id=?"
    cur.execute(sql, (student_id,))
    if cur.rowcount == 0:
        conn.close()
        abort(404, "Student not found")

    conn.commit()
    conn.close()
    return "", 204


@app.errorhandler(404)
@app.errorhandler(400)
def on_error(error):
    return jsonify({"status": error.code, "title": error.description}), error.code





def read_student(row):
    return {
        "id": row[0],
        "name": row[1],
        "birth_date": row[2],
        "gender": row[3],
        "address": row[4],
        "phone": row[5],
        "class": row[6],
        "group": row[7],
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
