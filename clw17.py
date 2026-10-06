'''
Exercise 18: product information displays product details and calculates total value.
'''
product = {
    "name": "Laptop",
    "brand": "Dell",
    "price": 75000,
    "quantity": 5
}
print("Product Name:", product["name"])
print("brand:", product["brand"])
print("price:", product["price"])
print("Available Quantity:", product["quantity"])

total_value = product["price"] * product["Quantity"]
print("Total Value:", total_value)

product["quantity"] -= 2

print("Quantity Ater selling 2 laptops:", product["quantity"])
