bands = {"Queen": "Bohemian Rhapsody", 
         "Bee Gees": "Stayin' Alive", 
         "U2": "One", 
         "Michael Jackson": "Billie Jean", 
         "The Beatles": "Hey Jude", 
         "Bob Dylan": "Like A Rolling Stone"}

print(len(bands))

for key in bands.keys():
    print(key)

print(bands.values())

for key, val in bands.items():
    print(key, val)

user_input = "Promise of the Real"
print(bands.get(user_input, user_input + " is not found in dictionary."))