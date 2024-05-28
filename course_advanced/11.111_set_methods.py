# .add() - metoda dodaje element podany jako argument (dowolnego typu) i dodaje do seta
scifi = {"star trek", "star wars", "halo"}
scifi.add("mass effect")

print(scifi)
scifi.add("star wars") # próba dodania elementu który juz jest w secie nie powoduje żadnej zmiany
                       # ani nie wyświetla żadnego błędu
print(scifi)

# .remove() - metoda usuwa element z seta 
fruits = {"apple", "orange", "banana", "tomato"}
fruits.remove("tomato")

print(fruits)

# fruits.remove("pear") # próba usunięcia nieistniejącego elementu wyświetli błąd

# .discard() - podobnie jak remove, ale nie wyświetla błędu kiedy próbujemy usunąć nieistniejący element
fruits = {"apple", "orange", "banana", "tomato"}
fruits.discard("pear")

print(fruits)

# .clear() - metoda czyści seta na którym została wywołana
mountains = {"Everest", "Kilimanjaro", "Fuji"}
print(mountains)
mountains.clear()
print(mountains)

# .copy() - metoda tworzy kopię seta
mountains = {"Everest", "Kilimanjaro", "Fuji"}
set_2 = mountains.copy()

print(set_2 is mountains) # sprawdzamy czy to są te same sety
                          # False znaczy że są to różne sety ale zawierają te same elementy
print(mountains)
print(set_2)   

# .union() - łączy dwa różne sety w jeden
set_1 = {1, 2, 3, 4, 5}
set_2 = {6, 7, 8, 9, 10}
set_3 = set_1.union(set_2)
print(set_3)
set_4 = set_2 | set_1 # ten sam efekt przynosi symbol "|" rurka nad enterem
print(set_4)

# .intersection() - metoda pozwala sprawdzić jakie są wspólne elementy z dwuch setów
set_1 = {4, 5, 6, 7, 8}
set_2 = {6, 7, 8, 9, 10}
set_3 = set_1.intersection(set_2)
print(set_3)

set_4 = set_1 & set_2
print(set_4)

# .difference() - subrtaction (odejmowanie)
set_1 = {4, 5, 6, 7, 8}
set_2 = {6, 7, 8, 9, 10}
set_3 = set_2 - set_1
print(set_3)
set_3 = set_1 - set_2
print(set_3)
set_3 = set_1.difference(set_2)
print(set_3)