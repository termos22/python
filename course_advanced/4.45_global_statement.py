def loc_ex():
    global fruit   # powoduje że funkcja zmienia wartość zmiennej globalnej
    fruit = "pear"
    print(fruit)

fruit = "apple"
print(fruit)
loc_ex()
print(fruit)
