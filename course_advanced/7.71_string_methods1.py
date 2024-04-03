all_low = "there are no capitals here."
print(all_low.upper())  # metoda upper powoduje że wszystkie litery są duże
print(all_low)          # metody nie zmieniają oryginalnego stringa

all_up = "THIS IS SHOUTING TEXT!"
print(all_up.lower())   # metoda lower powoduje że litery są małe

print("Mixed Case".isupper())  # metoda sprawdza czy w stringu są same duże litery i zwraca True lub False
print("ALL CAPS".isupper())

print("AAAHHH!".islower())
print("testtesttest=1".islower())

print("".isupper())
print("37&8.,?\"".islower())


print("SHOUT!".lower().isupper())

# pozostałe metody
# .isalpha()   - tylko litery
# .isalnum()   - tylko cyfry i litery
# .isdecimal() - tylko cyfry
# .isspace()   - tylko spacje
# .istitle()   - tylko stringi gdzie pierwsza litera każdego wyrazu jest pisana dużą literą
print("Batman".isalpha())
print("Batman123".isalpha())

print("Batman123".isalnum())
print("Batman".isalnum())
print("123".isalnum())

print("123".isdecimal())
print("3.14159".isdecimal())

print("  ".isspace())
print("                            ".isspace())
print("not just spaces".isspace())
print("not just spaces"[3].isspace())

print("The Empire Strikes Back".istitle())
print("Super Smash Broters: Ultimate!".istitle())  # działa również ze znakami interpunkcyjnymi i znakami specjalnymi

print("the great gatsby".title())

# .startswith() - zwraca True jeżeli string zaczyna się wyrażeniem z argumentu 
# .endswith()   - zwraca True jeżeli string kończy się wyrażeniem z argumentu
# obie funkcje są CASE SENSITIVE
print("this is a string".startswith("this"))
print("this is a string".endswith("this"))
print("this is a string".startswith("T"))


# .join() - łączy stringi. w pierwszym "" podajemy co ma być pomiędzy stringami
# następnie jako argument podajemy listę stringów, lista zawsze zamknięta jest w []
print("".join(["one", "two", "three"]))
print(" ".join(["one", "two", "three"]))
print(",".join(["one", "two", "three"]))
print(", ".join(["one", "two", "three"]))
print("...".join(["one", "two", "three"]))

# .split() - rozdziela stringi, w pzeciwieństwie do metody .join
# domyślnie metoda .split() rozdziela string po spacji
print("Eggs, Milk, Waffles, Bacon".split())
print("Eggs, Milk, Waffles, Bacon".split(","))
print("Eggs, Milk, Waffles, Bacon".split(", "))