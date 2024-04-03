user_int = int(input("Please enter an positive integer: "))
counter = user_int
summed = 0

while counter > 0:
    summed += counter
    counter -= 1

print("User entered " + str(user_int))
print("The summed integers is " + str(summed))
