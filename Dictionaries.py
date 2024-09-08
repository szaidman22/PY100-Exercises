# First Car

car = {
    'type': 'sedan',
    'color': 'blue',
    'mileage': '80_000'
}

# Adding the Year

car['year'] = 2003

print(car)

# Broken Odometer

car.pop('mileage')

# or use del car['mileage']

print(car)

# What Color?

print(car['color'])

# What's My Length?

print(len(car))

# Checking Key Existence

student = {
    'id': 123,
    'grade': 'B',
}

# student.get('name') is not None
# student.get('grade') is not None

print('name' in student)
print('grade' in student)

# Multiple Cars

truck = {
    'type': 'pickup',
    'color': 'red',
    'year': 1998
}

vehicles = {
    'Car': car,
    'Truck': truck
}
    
# Which Collection?

car_list = [
    ['type', 'sedan'],
    ['color', 'blue'],
    ['year', 2003]
]

# Divided by Two

numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}

half_numbers = []

for x in numbers.values():
    half_numbers.append(x // 2)

print(half_numbers)

# Labeled Numbers

# for item in numbers.items():
#     print(f'A {item[0]} number is {item[1]}')

for key, value in numbers.items():
    print(f'A {key} number is {value}.')