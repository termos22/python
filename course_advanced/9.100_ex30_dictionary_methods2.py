cons = {}.fromkeys("bcdfghjklmnpqrstvwxyz", "consonant")
for key, value in cons.items():
    print(key, value)

# lub można to wykonać tak

for key, value in {}.fromkeys("bcdfghjklmnpqrstvwxyz", "consonant").items():
    print(key, value)

fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
print(fast_food_items.pop("McDonald's"))


fast_food_items.popitem()
print(fast_food_items)
