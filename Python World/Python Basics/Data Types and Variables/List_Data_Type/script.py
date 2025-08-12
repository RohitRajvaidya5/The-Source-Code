# List
fruits = ['apple', 'banana', 'orange', 'pear', 'peach']

# Allowed Duplicates
marks = [100, 99, 99, 95, 19, 29]

# Get Unique elements from the list
numbers = [1, 2, 3, 4, 5, 11, 22, 11, 33, 33, 66, 44, 99, 100, 109, 100, 2, 3, 5, 6, 7]
ans = []

for number in numbers:
    if numbers.count(number) == 1:
        ans.append(number)

print(ans)

