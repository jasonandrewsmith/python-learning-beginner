contacts = {
    "number": 4,
    "students": [
        { "name": "Sarah Holderness", "email": "sarah@example.com" },
        { "name": "Harry Potter", "email": "harry@example.com" }
    ]
}

for student in contacts["students"]:
    print(student["name"])
    print(student["email"])