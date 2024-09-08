# Reading Error Messages

def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

find_first_nonzero_among(0, 0, 1, 0, 2, 0)
find_first_nonzero_among(1)

#TypeError: find_first_nonzero_among() takes 1 
# positional argument but 6 were given

# the wrong type was entered as an argument for the find first nonzero
# function. the function only takes one argument.

#TypeError: 'int' object is not iterable

# the wrong type was entered as an argument again. an integer was entered,
# which is not iterable. 

# in both cases, making the input a list (or other collection)
# would fix the error.

# Weather Forecast

import random

def predict_weather():
    sunshine = random.choice([True, False])

    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")

# the code was assigning a random string of true or false to
# the variable sunshine. this always evaluated to true.
# changing the randome choise to booleans fixed the issue.

# Multiply By Five

def multiply_by_five(n):
    return int(n) * 5

print("Hello! Which number would you like to multiply by 5?")
number = input()

print(f"The result is {multiply_by_five(number)}!")

# multiply_by_five needs to
# convert the input to an integer

# Pets

pets = { 'cat': 'pepe', 'dog': ['sparky', 'fido'], 'fish': 'oscar' }

pets['dog'].append('bowser')

print(pets)  # Output: {'cat': 'pepe', 'dog': 'bowser', 'fish': 'oscar'}

# Confucius Says

def get_quote(person):
    if person == 'Yoda':
        return 'Do. Or do not. There is no try.'
    if person == 'Confucius':
        return 'I hear and I forget. I see and I remember. I do and I understand.'
    if person == 'Einstein':
       return 'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'

print('Confucius says:')
print('"' + get_quote('Confucius') + '"')

# you weren't returning anything. Adding return statements fixes.

# Populate List

numbers = []

for i in range(1,6):
    numbers.append(i)

print(numbers)

# Dictionary Access

info = {'name': 'Srdjan', 'age': 38}

print(info.get('city','Unknown'))

# Matrix

sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(list(sub_list))
    # or matrix.append(sub_list.copy())

matrix[0][0] = "X"
print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]

# Find Maximum

def find_maximum(numbers):
    if not numbers:
        return None
    
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

print(find_maximum([45, 3, 10, 98, 22]))  # Expected 98
print(find_maximum([-1, 0, 5, 3]))         # Expected 5
print(find_maximum([-10, -3, -20, -2]))   # Expected -2

# Digit Product

def digit_product(str_num):
    digits = [int(n) for n in str_num]
    product = 1

    for digit in digits:
        product *= digit

    return product

result = digit_product('12345')
print(result)  # expected: 120, actual: 0