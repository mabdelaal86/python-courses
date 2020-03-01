#!/usr/bin/env python3

students = [
    {"id": "402", "name": "Manal", "address": "Giza", "age": 22, "gender": "Female", "class": "3", "phone": "0123456789"},
    {"id": "220", "name": "Samir", "address": "Cairo", "age": 19, "gender": "Male", "class": "1", "phone": "0100112233"},
    {"id": "223", "name": "Asmaa", "address": "Alex", "age": 19, "gender": "Female", "class": "1", "phone": "0111111111"},
    {"id": "317", "name": "Magdy", "address": "Alex", "age": 21, "gender": "Male", "class": "2", "phone": "0198765432"},
    {"id": "503", "name": "Hany", "address": "Giza", "age": 23, "gender": "Male", "class": "4", "phone": "0111222333"},
]

# find Males with age >= 21 to send their data for postponding army
for s in students:
    if s["gender"] == "Male" and s["age"] >= 21:
        print(s["id"], s["name"], s["address"])
