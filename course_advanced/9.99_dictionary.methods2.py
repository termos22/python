# .fromkeys() - metoda tworzy dict z podanych dwuch argumentów, 
            # pierwszy argment iterowalny używany jest jako keys (np.: lista albo string)
            # drugi argument używany jest jako wartości
ex_1 = {}.fromkeys(["address"], "1600 Pennsylvania Avenue NW")
print(ex_1)

ex_1a = {}.fromkeys("ad", "1600 Pennsylvania Avenue NW")
print(ex_1a)

ex_1b = {}.fromkeys("addr", "1600 Pennsylvania Avenue NW")
print(ex_1b)

ex_1c = {}.fromkeys(["brand"])
print(ex_1c)

# .pop() - metoda podobnie jak w listach usuwa parę elementów klucz: wartość (analogicznie dla dict)
ex_2 = {"make": "Honda", "model": "civic", "year": 2016}
popped = ex_2.pop("model")
print(ex_2)
print(popped)

# ex_2.pop("type") # jeżeli spróbujemy usunąć element, który nie istnieje wyskoczy błąd

# .popitem() - metoda pozwala usunąć ostatnią parę z dict bez konieczności podawania klucza
ex_3 = {"name": "bob", "age": 38, "ocupation": "accountant", "workplace": "H&R block"}
ex_3.popitem()
print(ex_3)

# ex_3.popitem("name") # jeżeli podamy metodzie argument to zwróci ona błąd 

