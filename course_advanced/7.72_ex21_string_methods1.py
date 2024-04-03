#1
mixed_case = "A Song of Ice and Fire"
#2
print(mixed_case.isupper())
#3
print(mixed_case.islower())
#4
print(mixed_case.upper())
#5
print(mixed_case.lower())
#6
print(mixed_case.istitle())
#7
title_case = mixed_case.title()
#8
print(title_case)
#9
print(mixed_case.startswith("A"))
#10
print(mixed_case.endswith("e"))
#11
words = mixed_case.split()
#12
print(words)
#13
print("".join(words).isalpha())
