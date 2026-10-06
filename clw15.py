'''
Excersise 16: Student Marks Dictonery Finds statistice from a dictonary of student matks.
'''
marks = {
    "Ram": 75,
    "Sita": 88,
    "Hari": 65,
    "Gita": 92,
    "john": 55
}
print("Student and Marks:")
for name, mark in marks.items():
    print(name, ":", mark)

total = sum(marks.values())
average = total / len(marks)
highest = max(marks.values())
lowest = min(marks.values())
top_student = max(marks, key=marks.get)

print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

