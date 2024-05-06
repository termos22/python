nested = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12))
nested_1 = (1, 2, 3, (4, 5, 6), (7, 8, 9), (10, 11, 12))

print(nested)
print(nested_1)

print(nested_1[4])
print(nested_1[5][1])

# metoda .count() - liczy ilość wystąpień elementu w tuple
repeat = (7, 3, 3, 3, 0, 0, 7, 0, 0)
print(repeat.count(7))
print(repeat.count(3))
print(repeat.count(0))

# metoda .index() - jeżeli wiadomo że dany element istnieje w tuple, metod wyświetli 
# numer indeksu.
# jeżeli tuple zawiera wiele wystąpień danego elementu, zostanie wyświetlony numer indeksu
# pierwszego wystąpienia
ints = (1, 1, 7)
print(ints.index(7))
print(ints.index(1))
print(ints.index(8))