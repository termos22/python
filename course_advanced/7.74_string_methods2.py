# .rjust() - justuje tekst do prawej
# .ljust() - justuje tekst do lewej
# jako argument podajemy liczbę int oraz jednozakowy string który będzie traktowany jako wypełniacz
# domyślnie jest to spacja. Liczba int symbolizuje łączną liczbę znaków w stringu
# funkcje dodają z lewej lub z prawej strony stringu spacje (lub znak podany jako argument) aby 
#uzyskać przesunięcie  
print("hello world".rjust(15))
print("hello world".ljust(15) + "four spaces later.")

print("hello world".rjust(15, "_"))
print("hello world".ljust(15, "*"))

# .center() - działa analogicznie do dwóch poprzednich ale ustawia stringa po środku
print("hello world".center(15))
print("hello world".center(15, "*"))

# .strip() - domyślnie usuwa ze stringu wszystkie spacje znajdujące się na początku i na końcu
# .rstrip() - domyślnie usuwa ze stringu wszystkie spacje znajdujące się z prawej strony
# .lstrip() - domyślnie usuwa ze stringu wszystkie spacje znajdujące się z lewej strony
# jako agument do powyższych metod można przesłać string który chcemy usunąć z głownego stringu
print("I had an exciting trip!!!11111")
print("I had an exciting trip!!!11111".strip("1"))
print("I had an exciting trip!!!11111".rstrip("1"))
print("I had an exciting trip!!!11111".lstrip("1"))

print("juice, bread, cheese, beef, bread".rstrip(", bread"))
print("juice, bread, cheese, beef, bread".rstrip(",ed arb")) # metoda rozpoznaje znaki więc nie jest ważna ich kolejność

print("blueblueyellowblue".strip("eulb"))

# .replace() - wyszukuje i zamienia string
print("Good morning.".replace("morning", "afternoon"))