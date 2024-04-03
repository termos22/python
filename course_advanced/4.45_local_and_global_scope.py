example = "hello world"       # zmienna globlna używana i rozpoznawalna w całym programie

def loc_ex():
    example = "this is a string"  # zmienna lokalna, używana wewnątrz funkcji
    return example


print(example)
print(loc_ex())

