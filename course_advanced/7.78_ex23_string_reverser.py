user_input = input("Please input a string: ")
reversed = ""

for item in range(len(user_input) - 1, -1, -1):
    reversed += user_input[item]

print(reversed)
