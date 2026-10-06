'''
Exercise 10: Student Marks list calculates statistics of sutdent marks.
'''
marks = [75, 82, 68, 90, 55, 88, 72, 95]
print("all marks:", marks)
print("total marks:", sum(marks))
print("Average marks:", sum(marks)/len(marks))
print("highest marks:", max(marks))
print("lowest marks:", min(marks))

count = 0
for mark in marks:
    if mark >= 75:
        count += 1
print("students scoring 75 or more:", count)
sorted_marks = sorted(marks, reverse=True)
print("marks from highest to lowest:", sorted_marks)
