indexes_example = ["carpet", "hardwood", "linoleum"]
print(indexes_example[1])

indexes_example2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(indexes_example2[2][0])
print(indexes_example[2][0])

# negative indexes
negative = [1, 2, 3, 4, 5]
print(negative[-1])
print(negative[-2])

# using items accessed by index in expressions
mixed = [False, 365, 4.24, "this is a string"]
print(mixed[2] + 1.76)
print("I have used \"" + mixed[-1] + "\" as an example too many times.")

# list slicing
sliced = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sliced[:4])
print(sliced[3:8])
print(sliced[6:])

# reassigning a list's items
example = [2, 4, 6, 8, 0]
print(example)
example[3] = 10
print(example)
example[1:4] = [3, 2, 1]
print(example)
example[4:7] = [7, 6, 5]
print(example)