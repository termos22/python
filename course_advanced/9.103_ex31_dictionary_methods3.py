internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
another_one = {"shroud": "Twitch"}

internet_celebrities.update(another_one)
print(internet_celebrities)

copy_internet_celebrities = internet_celebrities.copy()
print(copy_internet_celebrities)

internet_celebrities.clear()
print(internet_celebrities)
print(copy_internet_celebrities)


# rozwiązanie z kursu
internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
another_one = {"shroud": "Twitch"}
internet_celebrities.update(another_one)  # 2
gamers = internet_celebrities.copy()  # 3
internet_celebrities.clear()  # 4
print(internet_celebrities)  # 5
print(gamers)  # 6