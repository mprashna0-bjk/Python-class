'''
Exercise 14: Dictonary Keys and values Displays keys, values, and key-value pairs 
'''
books = {
    "title": "Python Basics",
    "author": "John Smith",
    "year": 2025,
    "price": 500
}
print("Keys:", books.keys())
print("Values:", books.values())
print("items:", books.items())

print("\nBook Details:")
for key, value in books.items():
    print(key, "=", value)
          
            