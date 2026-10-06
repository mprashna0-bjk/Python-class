'''
Exercise 15: Check if a key Exists Checks whether a given key exists in the dictonary.
'''
student = {
    "name": "Hari",
    "age": 19,
    "course": "Python",
    "city": "Lalitpur"
}
key = input("Enter a key:")

if key in student:
    print(key, "exists in the dictonary.")
else:
    print(key, "does not exist in the dictonary.")


