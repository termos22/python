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

print("elizabeth" in birth_years)