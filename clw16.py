'''
Excercise 17: Count items using a dictionary counts how many times each fruit apperars  
'''
fruits = {
    "apple", "banana", "apple", "orange", "banana", "apple", "mango", "orange", "banana"

}
count = {}
for fruit in fruits:
    if fruit in count:
        count[fruit] += 1
    else:
        count[fruit] = 1
print(count)