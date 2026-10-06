'''
Exercise 2: Add Items to a List
'''

students = ["Ram", "Sita", "Hari", "Gita", "John"]

students.append("Sam")
students.insert(0, "Anita")
students.insert(3, "Peter")

print("Updated list:", students)
print("Total students:", len(students))