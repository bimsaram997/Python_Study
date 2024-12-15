# Variables
age = 20
price = 19.5
firstName = "Bimsara"
isOnline = True

# Using an f-string
print(f"Name: {firstName} Age: {age} Price: {price} Online: {isOnline}")

# inputs
name  = input("What is your name? ")
print(f"hello {name}")

# Type conversions
birthYear =  input("input your birth year: ")
age = 2024 - int(birthYear)
print(f"Your age is {age}")

first  =  input("First: ")
second  =  input("Second: ")
sum = int(first) + int(second)
print(f"Sum Int is {sum}")

first  =  float( input("First: "))
first  =  input("First: ")
second  =  input("Second: ")
sum = float(first) + float(second)
print(f"Sum float is {sum}")

# Strings
word = "Hello Python"
# return new string
print(word.upper())
print(word.find('Python'))
print(word.replace('Python', 'PYTHON'))
print('Python' in word)

# Arithmatic operations
print(10 /3)
print(10//3)
x = 10
x+=3
print(x)

# operator precedence
x= 10+3*2
print(x)

# comparison operators
x =  3 > 2
print(x)

# logical expressions
price  = 25
print(price > 10 and price <30)
print(price > 10 or price > 30)
age  = 10
print(not age > 20)

# if condition
temp = 21
if temp > 30:
    print("Its' a hot day")
    print("Drink water")
elif temp > 20:
    print("It's a good day")
elif temp > 10:
    print("A cold day")
else:
    print("Very cold")

# Exercise    
weight = float(input("Enter Weight: "))
unit  =  str(input("Enter unit (K)Kg or (L)Lbs: "))

if unit.upper() == "K":
    converted = weight/0.45
    print(f"Weight is {converted}")
else:
    converted = weight * 0.45
    print(f"Weight is {converted}")

# while loop
i = 1
while i <= 5:
    print(i * "*")
    i+=1

# Lists
names = ["John", "Bob", "Marie", "Sam"]
names[0] = "Joe"
print(names)
print(names[0])
print(names[-1])
print(names[-2])
print(names[0 : 2])

numbers = [1,2,3,4,5,6]
numbers.append(7)
print(numbers)
numbers.insert(0, -1)
print(numbers)
numbers.remove(3)
print(numbers)
print (1 in numbers)
print(len(numbers))
numbers.clear()
print(numbers)

# for loop
numbers = [1,2,3,4,5,6]
for item in numbers:
    print(item)
print("While")
i=0
while i < len(numbers):
    print(numbers[i])
    i +=1

# ranges
numbers  = range(5, 10, 2)
print(numbers)
for number in numbers:
    print(number)
for number in range(5):
    print(number)

numbers = (1,2,3,1)
# tuples are immutable
print(numbers.count(1))
