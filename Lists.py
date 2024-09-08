# First Element

def first(list):
    if list:
        return list[0]
    else:
        return None

print(first(['Earth', 'Moon', 'Mars']))  # Earth

# Last Element

def last(list):
    if list:
        return list[-1]
    else:
        return None
    
# Add + Delete

energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']

energy.pop(0) # or energy.remove('fossil')

energy.append('geothermal')

print(energy)

# Alphabet

alphabet = 'abcdefghijklmnopqrstuvwxyz'

# or just to list(alphabet)

alphabet_list = [letter for letter in alphabet]

print(alphabet_list)

# Filter

scores = [96, 47, 113, 89, 100, 102]

sum = len([score for score in scores if score >= 100])

print(sum)

# Vocabulary

vocabulary = [
    ['happy', 'cheerful', 'merry', 'glad'],
    ['tired', 'sleepy', 'fatigued', 'drained'],
    ['excited', 'eager', 'enthused', 'animated'],
]

for lst in vocabulary:
    for word in lst:
        print(word)

# Equality

list1 = [2, 6, 4]
list2 = [2, 6, 4]

print(list1 == list2)

# I think they'll be equal but not the same object (?)

# Type

some_value1 = [0, 1, 0, 0, 1]
some_value2 = 'I leave you my Kingdom, take good care of it.'

isinstance(some_value1, list)
isinstance(some_value2, list)

# Travel

destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(location, list):
    if list.count(location):
        return True
    else:
        return False

#better solution:
# def contains(element, lst):
#     return element in lst

# def contains(item, lst):
#     return lst.count(item) > 0

contains('Barcelona', destinations)  # True
contains('Nashville', destinations)  # False

# Passcode

passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']

'-'.join(passcode)

# Checking items off the grocery list

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

while grocery_list:
    print(grocery_list[0])
    grocery_list.pop(0)
    