#Multiply

def multiply(num1, num2):
    return num1 * num2

multiply(12, 4)

#Print Quote

def bruce_eckel_quote():
    print('Python is executable pseudocode.')

bruce_eckel_quote()

#return value is none

#Cite the Author

def cite(author, quote):
    print(f'{author} said: "{quote}"')

cite('Bruce Eckel', 'Python is executable pseudocode.')

#Squared Number

def squared_number(number):
    return number * number

squared_number(3)

#Display Division

#multiples of 3 is never invoked with () so nothing will print

#Three-way Comparison

def compare_by_length(string1, string2):
    if len(string1) < len(string2):
        return -1
    elif len(string1) == len(string2):
        return 0
    else:
        return 1

compare_by_length('patience', 'perseverance') # -1
compare_by_length('strength', 'dignity')      #  1
compare_by_length('humor', 'grace')           #  0

#Transformation

string = 'Captain Ruby'

new_string = string.replace('Ruby', 'Python')

#Internationalization 1

def greet(iso_code):
    match iso_code:
        case 'en': 
            print('Hello!')
        case 'fr':
            print('Bonjour!')
        case 'es':
            print('Hola!')
        case 'de':
            print('Guten Tag!')
        case _:
            print("I don't know you")

print(greet('en'))         # Hi!
print(greet('fr'))         # Salut!
print(greet('pt'))         # Olá!
print(greet('de'))         # Hallo!
print(greet('sv'))         # Hej!
print(greet('af'))         # Haai!

#Locale Part 1

def extract_language(locale):
    return locale[0:2]

print(extract_language('en_US.UTF-8'))      # en
print(extract_language('en_GB.UTF-8'))      # en
print(extract_language('ko_KR.UTF-16'))     # ko

#Locale Part 2

def extract_region(locale):
    return locale[3:5]

print(extract_region('en_US.UTF-8'))    # US
print(extract_region('en_GB.UTF-8'))    # GB
print(extract_region('ko_KR.UTF-16'))   # KR

#Internationalization 2

def local_greet(locale):
    lang = locale[0:2]
    reg = locale[3:5]
    if lang == 'en':
        match reg:
            case 'US':
                print("Howdy Partner")
            case 'GB':
                print("Good day to you sir")
            case 'AU':
                print("G'day mate")
            case _:
                print('What English speaking country is this?')
    else:
        match lang:
            case 'fr':
                print('Bonjour!')
            case 'es':
                print('Hola!')
            case 'de':
                print('Guten Tag!')
            case _:
                print("I don't know you")

print(local_greet('en_US.UTF-8'))
print(local_greet('en_GB.UTF-8'))
print(local_greet('en_AU.UTF-8'))

print(local_greet('op_th.UTF-8'))

print(local_greet('fr_FR.UTF-8'))
print(local_greet('fr_CA.UTF-8'))
print(local_greet('fr_MA.UTF-8'))