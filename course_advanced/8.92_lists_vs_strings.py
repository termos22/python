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
import copy
ex_12 = [1, 2, 3, 4, 5]
ex_13 = copy.deepcopy(ex_12)
print(ex_12)
print(ex_13)
ex_13[2] = 4
print(ex_12)
print(ex_13)
ex_14 = ex_13
ex_14[4] = 6
print(ex_12)
print(ex_13)

#listy mogą zajmować wiele linii, przykład
ex_15 = ["bush",
         "fern",
         "tree",
         "moss"]

print(ex_15)

# kontynuowanie poleceń w wielu liniach za pomocą \
ex_16 = 2 + \
        4 + \
        1
print(ex_16)

ex_17 = "The Emp\
ire Strkes \
Back"

print(ex_17)

ex_18 = "hello " + \
        "world"
print(ex_18)