# metody do słowników
# .keys() - wyświetla wszystkie klucze ze słownika
# .values() - wyświetla wszystkie wartości przypisane kluczom
# .items() - 
# .get() - 

birth_years = {1994: "bill", 1969: "emily", 1982: "elizabeth", 2000: "turner"}

print(birth_years.keys())
print(birth_years.values())
print(birth_years.items())


for key in birth_years.keys():
    print(key)

for val in birth_years.values():
    print(val)

for key, val in birth_years.items():
    print(key, val)

print(type(birth_years.keys()))
print(type(birth_years.values()))
print(type(birth_years.items()))

print(list(birth_years.keys()))
print(list(birth_years.values()))
print(list(birth_years.items()))


# opeator "in" oraz "not in"
print("elizabeth" in birth_years)
print(1982 in birth_years)
print("elizabeth" in birth_years.values())

# .get() - metoda do wyciągania wartości po podanym kluczu
if 1975 in birth_years:
    print(birth_years[1975])
else:
    print("1975 is not a key in birth_years.")

print(birth_years.get(1975, "1975 is not a key in birth_years."))

# other things you should know about dicctionaries
print(birth_years) 
# dict jest traktowany jako referencja więc przypisanie nowej wartości
# modyfikuje cały dict
people = birth_years
people[1982] = "madeline"
print(birth_years)

# dict można podzielić na więcej linii ale trzeba pilnować żeby wszystkie klucze byly
# w jednej linii pod sobą
birth_years = {1994: "bill", 
               1969: "emily", 
               1982: "elizabeth", 
               2000: "turner"}

print(len(birth_years))
