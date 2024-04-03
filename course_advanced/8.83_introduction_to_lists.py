example_list_1 = [5, 4, 3, 2, 1] # lista z wartościami integer
example_list_2 = [2.718, 9.31] # lista z wartościami float
example_list_3 = ["blue", "green", "red", "yellow", "purple", "orange"] # lista z wartościami string
example_list_4 = [True, False, False, True, False, True, True, False, True] # lista z wartościami boolean
example_list_5 = [[1, 2, 3], [4, 5], [6, 7, 8, 9]] # lista z wartościami typu lista
example_list_6 = [10, 3.14159, "tree", False, [1, 2, 3]] # lista z wartościami różnego typu

# funkcja list() - konwertuje string z argumentu na listę wartości
print(list("blah"))

# operatory "in" oraz "not in" wsazują czy zadana wartość znajduje się lub nie na podanej liście
checked_list = [1, 2, 3, 4]
print(1 in checked_list)  # wyświetli True ponieważ 1 jest na liście
print(8 in checked_list)  # wyświetli False ponieważ 8 nie ma na liście
not_in_example = 8 not in checked_list  # przypisujemy zmiennej wartość boolean w zależności od tego czy 8 nie ma na liście
print(not_in_example)  # wyświetla wartość zmiennej, poda True ponieważ 8 nie ma na liście

not_in_example = 3 not in checked_list  # przypisujemy zmiennej wartość boolean w zależności od tego czy 3 nie ma na liście
print(not_in_example) # wyświetla wartość zmiennej, poda False ponieważ 3 jest na liście