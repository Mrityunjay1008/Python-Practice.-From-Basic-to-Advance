# dictionary (key, value)
student = {
    "name": "Mrityunjay",
    "age": 21,
    "marks": {
        "Physics": 90,
        "Chemistry": 80,
        "Maths": 70
    },
    "subjects": ["Physics", "Chemistry", "Maths"],
}

# Access values
print(student["name"])
print(student["marks"]["Physics"])
print(student["subjects"][2])
print(student.get("phone", "Not Found"))

print(student.keys())
print(student.values())
print(student.items())

print(len(student))

# Add & Update
student["phone"] = 1234567890
student["age"] = 22

student.update({
    "phone": 999999999,
    "age": 81,
    "marks": {
        "SST": 91,
        "Hindi": 81,
        "GK": 71
    }
})

# Delete
del student["phone"]
student.pop("name") # this will delete the name key and return it

# Loop
for key, value in student.items():
    print(key, value)
