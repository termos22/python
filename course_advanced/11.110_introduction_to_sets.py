# sety nie mogą mieć zdupolikowanych elementów
# elementy w setach ine są indeksowane tak jak elementy w słownikach

# tworzenie setów
set_1 = {9, 8, 7, 6}
set_2 = set({"a", "b", "c", "d", "e"})
print(set_1)
print(set_2)

set_3 = {9, 8, 8, 8, 7, 6} # jeżeli set zawiera elementy zduplikowane zostana one zignorowane
print(set_3)

# żeby utworzyć pusty set trzeba użyć funkcji set()
# ponieważ uzycie samych nawiasów {} spowoduje utworzenie pustego słownika

empty_set_4 = set()
print(empty_set_4)

# użycie funkcji range() w celu utworzenia seta
set_5 = set(range(1, 12, 2))
print(set_5)

# set może przechowywać elementy różnych typów

set_6 = {"a", 3.14, 18, True}
print(set_6)

# sety nie sa indeksowane więc nie można wyświetlić elementu po jego indeksie
# można za to wyśiwetlic wszystkie elementy seta jeden po drugim za pomocą pętli

set_7 = {3, 6, 9, 12, 15}

for dupa in set_7:
    print(dupa)
# sprawdzanie czy w secie występuje jakiś szukany element
set_8 = {3, 6, 9, 12, 15}
print(12 in set_8)

# zastosowanie setów
# - kiedy chcemy posadać pewną grupę elementów ale nie chcemy tryzmać duplikatów
# - kiedy nie zależy nam na kolejności zapamiętanych elementów

olympic_cities = ["Athens", "Paris", "St. Louis", "London","Stocholm", "Berlin", "Antwerp"
                  "Chamonix", "Paris", "St. Moritz", "Amsterdam", "Lake Placid",
                  "Garmisch-Partenkirchen", "Berlin", "Sapporo Garmisch-Partenkirchen",
                  "Tokyo Helsinki", "Cortina d'Ampezzo", "London", "St. Moritz", "London",
                  "Oslo", "Helsinki", "Cortina d'Ampezzo", "Melbourne", "Stockholm", "Squaw Valley",
                  "Rome", "Innsbruck", "Tokyo", "Grenoble", "Mexico City", "Sapporo", "Munich",
                  "Innsbruck", "Montreal", "Lake Placid", "Moscow", "Sarajevo", "Los Angeles",
                  "Calgary", "Seoul", "Albertville", "Barcelona", "Lillehammer", "Atlanta", "Nagano",
                  "Sydney", "Salt Lake City", "Athens", "Turin", "Beijing", "Vancouver", "London",
                  "Sochi", "Rio de Janeiro", "Pyeongchang", "Tokyo", "Beijing", "Paris",
                  "Milan Cortina d'Ampezzo", "Los Angeles", "Brisbane"
                  ]
print(set(olympic_cities))
print(len(olympic_cities))
print(list(set(olympic_cities)))
print(len(list(set(olympic_cities))))