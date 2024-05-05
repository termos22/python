# .clear() - metoda czyści słownik na którym została uruchomiona, nie bieże argumentów
ex_1 = {1: "England", 2: "Scotland", 3: "Wales", 4: "Northern Ireland"}
print(ex_1)
ex_1.clear()
print(ex_1)

# .copy() - zwraca kopię słownika (zamiast odwoływać sie do oryginału przez referencję)
birth_years = {1994: "bill", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
print(birth_years)
people = birth_years.copy()
people[1982] = "madeline"
print(birth_years)
print(people)

# .update() - metoda pozwala dodawać pary klucz: wartość do słownika z innego słownika lub 
            # nadpisać wartości w jednym słowniku inymi z drugiego słownika
city_info = {"country": "Canada", "province": "Ontario", "City": "Toronto"}
population = {"population": 2930000}
city_info.update(population)
print(city_info)


city_info = {"country": "Canada", "province": "Ontario", "City": "Toronto"}
population = {"population": 2930000}
city_info.update(population)
city_info["population"] = 3000000
print(city_info)
city_info.update(population)
print(city_info)

# jeżeli chcemy zrobić .update() z pustym słownikiem metoda update zwróci niezmieniony słownik
city_info = {"country": "Canada", "province": "Ontario", "City": "Toronto"}
city_info.update({})
print(city_info)


