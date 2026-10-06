'''
Exercise 9: Remove duplicate values creates a new list containing only unique values. 
'''
numbers = [10, 20, 10, 30, 20, 40, 10, 50, 30]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print("Unique value:", unique_numbers)
