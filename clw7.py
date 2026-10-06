'''
Exercise 8: shorting a list.
'''
numbers = [45, 12, 78, 3, 56, 28, 10]
print("Original list:", numbers)

ascending = sorted(numbers)
print("ascending order:", ascending)

descending = sorted(numbers, reverse=True)
print("descending order:", descending)

print("smallest number:", min(numbers))
print("largest number:", max(numbers))

names = ["Ram", "Sita", "Hari", "Gita", "John"]
names.sort()
print("Sorted Names:", names)