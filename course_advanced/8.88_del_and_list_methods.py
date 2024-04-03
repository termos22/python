# del - pozwala usunąć elementy z listy
planets = ["pluto", "mars", "earth", "venus"]
print(planets)
del planets[0] # usuwa indeks 0 z listy, pozostałe elementy z listy przesuwają się do początki
print(planets)


# metoda .remove() 
planets = ["pluto", "mars", "earth", "venus"]
print(planets)
planets.remove("pluto")
print(planets)


colors = ["blue", "red", "white", "blue", "orange", "blue"]
print(colors)
colors.remove("blue") # remove usuniejedynie pierwszy w koleności pasujący element
print(colors)

# różnica pomiędzy del i .remove()
# del odszukuje item po jego index'ie
# .remove() odszukuje item po tym co zostało podane w argumencie metody


# metoda .append() dodaje do listy item który podany został jako argument
# item ten pojawi się na końcu listy
pets = ["cat", "dog", "parrot"]
print(pets)
pets.append("fish")
print(pets)


# metoda .insert() - dodaje item do listy ale pozwala podać index na miejscu którego dany item ,a się pojawić
pets = ["cat", "dog", "parrot"]
print(pets)
pets.insert(1, "turtle")
print(pets)


# metoda .sort() - pozwala sortować listy zbudowane z liczb lub stringów
num_list = [2.718, 4, -19, 10000, 0]
print(num_list)
num_list.sort()
print(num_list)

str_list = ["Ringo", "John", "George", "Paul"]
print(str_list)
str_list.sort()
print(str_list)

num_list.sort(reverse=True) # sortuje listę w kolejności odwrotnej
print(num_list)
str_list.sort(reverse=True) # sortuje listę w kolejności odwrotnej
print(str_list)
# sortowania nie można wykonać na listach zawierających rózne typy itemów
mixed = [False, 5.67, "string", -2]
# mixed.sort() # wyświetli błąd
print(mixed)

mixed2 = [False, 5.67, -2]
mixed2.sort() # wartości boolowskie traktowane są jako 0 i 1 więc jeżeli na liście niema stringów
print(mixed2) # to możemy ją posortować

# metoda .sort() - tak na prawdę nie używa kolejnoąci alfabetycznej a ASCIIbetical order
# to znaczy że duże litery będą ustawiane przed ich małymi odpowiednikami
ASCIIbetical = ["Andy", "kiwi", "apple", "Karen", "Brian", "banana"]
ASCIIbetical.sort()
print(ASCIIbetical)

ASCIIbetical.sort(key=str.lower) # pozwala sortować w kolejności alfabetycznej
print(ASCIIbetical)

# metoda .index() pozwala odszukac numer indexu na liście dla wartości podanej jako argument
metals = ["copper", "gold", "silver", "iron"]
print(metals.index("silver"))

# print(metals.index("platinum")) # wyświetli błąd ponieważ platyny nie ma na liście

numbers = [4, 3, 2, 1, 0, 1, 2, 3, 4]
print(numbers.index(3))

# metoda .pop() - służy do usuwania i przywracania itemów na listach
# usunięty item może być przypisany do zmiennej
bands = ["Queen", "Led Zeppelin", "The Beatles", "MUSE", "Radiohead"]
end = bands.pop()
print(bands)
print(end)

end = bands.pop(3)
print(bands)
print(end)
