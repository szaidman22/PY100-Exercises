#Part 1
#will print 20

#Part 2
x = 10

def my_function():
    global x
    x = x + 5
    print(x)

my_function()

#Part 3

def my_function():
    a = 1

    if True:
        print(a)

my_function()

# prints 1

#Part 4

a = 1

def my_function():
    print(a)

my_function()

#prints 1

#Part 5

a = 1

def my_function():
    print(a)
    a = 2

my_function()

#UnboundLocalError: local variable 'a' referenced before assignment

# Part 6

a = 1

def my_function():
    a = 2

my_function()
print(a)

# will print 1

# Part 7

a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)

#will print 2

# Part 8

print(greeting)

greeting = 'Hello world!'

#this will give an Name error

# Part 9

a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)

# will print 7

# Part 10

b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)

# will print [10, 2, 3]