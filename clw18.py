'''
Exercise 19: Simple student database performs operations on a student databse
'''
students = {
    101: {"name": "Ram", "age": 20, "course": "python"},
    102: {"name": "sita", "age": 21, "course": "java"},
    103: {"name": "Hari", "age": 19, "course": "python"}

}

print ("All Students:")
print(students)

print("\nDetails of student 102:")
print(students[102])

students[103]["couese"] = "Data Science"

students[104] = {
    "name": "John",
    "age": 22,
    "course": "java"
}

del students[101]

print("\nFinal Dictionary:")
print(students)