# listy i stringi zawierają itemy z indexami
# listy = mutable - czyli itemy można zmieniać, usuwać czy dodawać
# stringi = immutable

ex_1 = [1, 2, 3]
print(ex_1)
ex_1[1] = 5
print(ex_1)
ex_2 = "123"
print(ex_2)
# ex_2[1] =5    zmiana elementu w stringu nie jest możliwa 
ex_2 = "153"   # żeby zmienić jeden element trzeba przypisać nowy zmieniony string
print(ex_2)

# Creating new strings from old strings
ex_3 = "No, you can't."
ex_4 = "Yes" + ex_3[3:11] + "!"
print(ex_3)
print(ex_4)

# references
ex_5 = 3.14159
ex_6 = "coconut"
ex_7 = ex_5
ex_8 = ex_6
print(ex_7)
print(ex_8)

ex_9 = [1, 2, 3, 4, 5]
ex_10 = ex_9
ex_10[2] = 4
print(ex_9)
print(ex_10)

# Why does Python have references?
# copy module and deepcopy()
