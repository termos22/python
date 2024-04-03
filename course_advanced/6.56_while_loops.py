counter = 0

while counter < 5:
    print(counter)
    counter += 1


# avoiding infinite loops
    
# counter = 1           pętla będzie wykonywana w nieskończoność ponieważ 
# while counter < 6:    licznik nie jest zwiększany przez co warunek zakończenia 
#    print(counter)     pętli nie zmieni się a FALSE.
