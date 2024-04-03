ex_1 = 'This is a string!'
ex_2 = "This is also a string"
ex_3 = '1984!'
ex_4 = "LiVe LONG and PRosPEr."
ex_5 = "!@#$%^&*()_-=+=/."
ex_6 = ""
ex_7 = "0123456"
ex_8 = "orange"
print(ex_8[2]) # drukuje 3 znak ze stringa (index zaczyna się od 0 dla tego 2 daje w sumie 3 znak)
print("apple"[4])

ex_10 = "apricots"
print(ex_10[:3]) # drukuje znaki stringa od początku do znaku z indeksem 3
print(ex_10[2:5]) # drukuje znaki z przedziału zaczynając od indeksu 2 i kończąc na indeksie 5
print(ex_10[4:]) # drukuje znaki zaczynając od znaku z indeksem 4 aż do konca stringa

print("pecan" + " " + "pie") # łączy 3 stringi w jeden

concatenated = "R2" + "-" + "D2"
print(concatenated)
print(concatenated[3])
print(concatenated[1:4])

unchanged = "forrest gump"
sliced = unchanged[6:]
print(sliced)
print(unchanged)
print(unchanged[10])
print(unchanged)
