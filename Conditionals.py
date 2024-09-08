#Truthy vs. Falsy

#falsy values are 0, None, empty collections, and False

#Yes? No? Part 1

import random
random_number = random.randint(0, 1)

if random_number:
    print('Yes!')
else:
    print('No.')

#Yes? No? Part 2

'Yes!' if random_number else 'No.'

#Check the Weather, Part 1

weather = 'sdfs'

if weather == 'sunny':
    print("It's a beautiful day!")
elif weather == 'rainy':
    print("It's a pensive day.")
else:
    print("Let's stay inside.")

#Match-Case:

animal = 'horse'

match animal:
    case 'duck':
        print('quack')
    case 'squirrel':
        print('nook nook')
    case 'horse':
        print('neigh')
    case 'bird':
        print('tweet tweet')
    case _:
        print('*cricket*')

#this will print neigh

#Check the Weather, Part 2

weather = 'rainy'

match weather:
    case "sunny":
       print("It's a beautiful day!")
    case "rainy":
       print("It's a pensive day.")
    case _:
       print("Let's stay inside.")

#Logical Conditions 1

if False or True:
    print('Yes!')
else:
    print('No...')

#False or True will evaluate to truthy, so Yes! will print

#Logical Conditions 2

if True and False:
    print('Yes!')
else:
    print('No...')

# True and False evaluates to falsy, so No... will print

#Logical Conditions 3

sale = True
admission_price = 5.25 if not sale else 3.99

print(f"${admission_price}")

#the code will print $3.99

#Are we moving?

speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)

#will print True

# I think we needed the parentheses