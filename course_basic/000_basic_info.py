# single line comment

""" This is comment
do not assign it 
to a variable """

print("Hello world")
print('Hello world')

name = "adam"
print(name)
print(type(name))

# basic datattypes in Python
# String
a = "This is string"  # można używać podwójnego cudzysłowu
b = 'This is also a string' # lub pojedynczego

# Integer
c = 10
d = 2
e = 200

# Float
f = 1.45

# List
g = [1,2,3,4,5] # zawiera elementy tego samego typu
print(g[2]) # drukuje 3 element z listy, numerowanie list zaczyna się od 0

# Tuple
h = (1,2.45,3,"adam",5) # może składać się z elementów róznego typu
print(h[3])

# Tuple is immutable, you can't change values of tuple
# List is mutable, values can be changed

a_list = [1,2,3]
a_tuple = (1,2,3)

a_list[0] = 3
print(a_list)

a_tuple[0] = 3 # this line generates an error: TypeError: 'tuple' object does not support item assignment



# Boolean
i = True
j = False

# Dictionary
movie = {
    "Name":"John Wick 4",
    "Status":"Watched"
}
print(movie["Status"])


# imput data
message = input("Please write a short message: ")
print(message)

# If statements
# used to execute code conditionaly

# if true
    # run this code
# else
    # run this code

x = 25
if x > 10:
    print("X is greater than 10.")
else:
    print("X is less than 10.")


# FOR Loop
# Repeat a specyfic task for multiple item

movies = ["JW4", "Blue Beetle", "Endgame", "RRR"]
for movie in movies:
    print(movie)

for i in range(1,11): # drukuje liczby 1 do 10
    print(i)

# While loop
# Loop code through code as long as
# some condition is True
    
x = 0

while x<=5:
    print(x)
    x += 1

# Function
# To write a block of code that can be reused
def add(a,b):
    return a+b

c = add(60,9)
print(c)

# use other's code in your code
# using import keyword

from math import *  # importing everything form math module

print(pi)

# Classes
# Used to represent real world things in code
# Like a blueprint

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def name(self):
        long_name = f"Name : {self.year} {self.brand} {self.model}"
        return long_name.title()
    
# Object created using Class
# is an instance of class
    
my_car = Car("Audi","A4",2012)
print(my_car.year)
print(my_car.name())

my_car2 = Car("Lexus","ES300",2019)
print(my_car2.year)
print(my_car2.name())

# Inheritance
#Using code of original class to create a newe one
#Original class = Parent class
#New class = Child Class

class ElectricCar(Car):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)
        self.battery_size = 75


    def Speak(self):
        speech = f"I'm {self.brand} {self.model}"
        return speech
    
new_car = ElectricCar("Tesla","Y",2019)
print(new_car.Speak())

