# wstęp do słowników DICTIONARIES
consoles = {"nintendo": "wii", "microsoft": "xbox", "sony": "playstation"}

#accessing dict by a key
print(consoles["microsoft"])
val = consoles["microsoft"]
print(val)

print("The " + consoles["sony"] + " 4 is Sony's newest gaming console.")

# słowniki mogą składać sie z różnych typów danych
mohs_hardness = {9:"corunndum", 10: "diamond"}
floats = {1.23: 1000, 3.14159: 10000, 2.718: 100000}
mixed = {"string": 1, 10210: 2, 4.976: 3, False: 4}

# dictionaries are unordered
print([2, 4, 6] == [2, 4, 6])
print([2, 4, 6] == [6, 4, 2]) # listy muszą mieć ten sam układ elementów żeby były soie równe

first = {0: 2.1, 1: 2.2, 2: 2.3, 3: 2.4}
second = {2: 2.3, 0: 2.1, 3: 2.4, 1: 2.2}
print(first == second)

# próba odwołania się do klucza który nie istnieje kończy sie błędem
third = {0: 2.1, 1: 2.2, 2: 2.3, 3: 2.4}
# print(third[4])

# sprawdzanie czy w słowniku istnieje klucz
print(0 in third)
print(1 not in third)