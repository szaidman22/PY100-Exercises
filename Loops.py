# Loop and Print

for num in range(0,11,2):
    print(num)
#expect 0,2,4,6,8,10

#Countdown
for i in reversed(range(1,11)):
    print(i)
print('Launch!')

for i in range(10,0,-1):
    print(i)
print('Launch!')

#Triple Greeting

greeting = 'Aloha'

for _ in range(0,3):
    print(greeting)

#Take Two

for x in range(1,101):
    print(x * 2)

#Looping over List Elements

lst = [1, 3, 7, 15]
index = 0

while index < len(lst):
    print(lst[index])
    index += 1

#Greet Your Friends

friends = ['Sarah', 'John', 'Hannah', 'Dave']

for friend in friends:
    print(f'Hello, {friend}!')

#Continue

cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
          'Vienna', None, 'London', 'Beijing', None]

for city in cities:
    if city is None:
        continue
    print(len(city))

#And on and on and on

#the code keeps running because nothing ever breaks the loop.
#it is always True

while True:
    print("and on")
    break

#Finding Nemo

fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']

for fish in fish_list:
    print(fish)
    if fish == 'Nemo':
        break

#Loop on Command

while True:
    print('Should I stop looping?')
    answer = input()
    if answer == 'yes':
        break