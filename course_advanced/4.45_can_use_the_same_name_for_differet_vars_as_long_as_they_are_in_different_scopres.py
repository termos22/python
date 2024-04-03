# You can use the same name for differet vars 
# as long as they are in different scopres.


def loc_ex1():
    fruit = "pear"
    print(fruit)


def loc_ex2():
    fruit = "banana"
    print(fruit)


fruit = "apple"
loc_ex1()
loc_ex2()
print(fruit)
