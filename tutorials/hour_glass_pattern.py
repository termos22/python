row = int(input("Enter number of rows: "))

print("Generated Hourglass Pattern is: ")
#Upper-Half
for i in range (row, 0, -1):
    for j in range(row-i):
        print(" ", end="")
    for j in range(1, 2*i):
        print("*", end="")
    print()

#Lower-half
for i in range (2, row+1):
    for j in range(row-i):
        print(" ", end="")
    for j in range(1, 2*i):
        print("*", end="")
    print()
