'''
Exercise 13: Remove Dictonary Items Removes keys from a dictonery.
'''

employee = {
    "name": "John",
    "age": 30,
    "department": "IT",
    "salary": 50000,
    "city": "Kathmandu"
}
del employee["age"]
del employee["city"]

print('Dictonary after removal:', employee)

removed_value = employee.pop("email", "Key not found")
print("email removal result:", removed_value)
