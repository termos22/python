tuple_1 = ("a", "b", "c", "d", "e")
tuple_2 = (2.718, False, [1, 2, 3])
tuple_3 = (1, 1, 0, 0, 0)

tuple_4 = (5, 4, 3, 2, 1)

tuple_5 = tuple([3.14, 2.205, 10])
tuple_6 = tuple("edcba")

print(tuple_5)
print(tuple_6)

tuple_7 = tuple({"a": 1, "b": 2, "c": 3})
print(tuple_7)

tuple_8 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tuple_8[2])
print(tuple_8[:8])
print(tuple_8[2:7])
print(tuple_8[3:])


# tuple jest immutable czyli dane wewnątrz nie mogą być zmienione
tuple_8 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# tuple_8[0] = "a" ta linia spowoduje wyświetlenie błędu 

tuple_9 = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
tuple_10 = ("Fall", "Winter", "Spring", "Summer")
tuple_11 = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

tuple_12 = (1, 3, 5)
list_1 = [1, 3, 5]

print(tuple_12.__sizeof__())
print(list_1.__sizeof__())

occupation = {("Angus", "Young"): "musician",
              ("Narendra", "Modi"): "prime minister",
              ("Richard", "Branson"): "entrepreneur",
              ("Quentin", "Tarantino"): "fimmaker"
              }

seven_wonders = {("29°58'44N", "31°08'02E"): "The Great Pyramid of Giza, Egipt",
                 ("33°13'23N", "43°40'45E"): "Hanging Gardens of Babylon",
                 ("37°38'18N", "21°37'47E"): "Archaeological Site of Olympia, Greece",
                 ("37°55'33N", "23°59'36E"): "Temple of Artemis at Ephesus",
                 ("37°02'16N", "27°25'26E"): "Mausoleum at Halicarnassus",
                 ("36°26'02N", "28°13'03E"): "Rhodes, Greece",
                 ("31°12'51N", "29°53'28E"): "Lighthouse of Alexandria, Egipt"
                 }
