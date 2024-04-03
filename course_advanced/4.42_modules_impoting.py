
# importowanie całego modułu
import random                 # impotuje moduł generowania losowych elementów

print(random.randint(1, 10))  # drukuje losową liczbę integer z zakresu 1-10


# importowanie wybranej funkcji z modułu
from random import randint    # importuje funkcję randint zmodułu random

print(randint(10, 20))        # przykład użycia zaimportowanej funkcji


# import uniwersalny wszystkich funkcji z modułu
from random import *          # importuje wszystkie funkcje z modułu random

print(random())
