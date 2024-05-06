major_cities = ("Tokyo", "London", "New York", "Shanghai", "Sydney")

for city in major_cities:
    print(city)

count = 0
while count < len(major_cities):
    print(major_cities[count])
    count += 1

backwards = len(major_cities) - 1
while backwards >= 0:
    print(major_cities[backwards])
    backwards -= 1

# użycie step (krok) przy cięciu tuple  

ints = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(ints[::3])   # co trzeci element
print(ints[1::2])  # tylko parzyste indeksy
print(ints[7::-1]) # w stecz zaczynając od 8 indeksu
print(ints[8::-2]) # tylko nieparzyste indeksy wstecz