# metoda .setdefault() - pozwala na dodanie kolejnego klucza do słownika nie wiedząc czy już taki istnieje
#  
computers = {"Google": "ChromeBook", "Apple": "MacBook", "Microsoft": "Surface Pro"}

if "Lenovo" not in computers:
    computers["Lenovo"] = "ThinkPad"

print(computers)

# lub wersja z metodą .setdefault()
computers.setdefault("Lenovo", "ThinkPad")


# użycie metody .setdefault() na słowniku który już zawiera takie dane nie spowoduje zmiany wartości klucza.
computers.setdefault("Lenovo", "IdeaPad")
print(computers)

computers.setdefault("Apple", "MacBook PRO")
print(computers)
