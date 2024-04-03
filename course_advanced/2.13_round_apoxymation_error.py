print(1.23 + 2.80) # wynik niewłaściwy z powodu błędu obliczania liczb typu float (spowodowane naleciałościamiu z języka C)
# przykłady jak sobie radzić z takimi problemami
ex2 = (123 +280) / 100 # mnożenie wyażenia przez wielokrotność 10 aby pozbyć się liczby typu float a następnie podzielenie wyniku przez tę samą wielokrotność liczby 10
print(ex2)

ex3 = 1.23 + 2.80
print(round(ex3, 2)) # użycie funkcji round(liczba, ilość miejsc po przecinku)
print(round(ex3, 6))