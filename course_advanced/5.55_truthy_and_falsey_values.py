strings_example = input("Enter any string other than an empty one.")

if strings_example:                                # ten kod działa mimo że nie porównujemy wartości do czegoś. wproadzenie dowolnej wartości powoduje że zmienna coś zawiera 
    print("thank you for entering something.")     # a to powoduje że warunek zostaje spełniony.
else:
    print("You did not enter a string.")



if strings_example != "":                          # dobrą praktyką jest jednak porównanie zmiennej do czegoś (na przykład do pustego stringa)
    print("thank you for entering something.")     # ułatwia to zrozumienie kodu
else:
    print("You did not enter a string.")


# dla liczb integer wartość "0" jest przyjmowana jako FALSEY, każda inna będzie traktowana jako TRUTHY
# dla liczb float wartość "0.0" jest przyjmowana jako FALSEY, każda inna będzie traktowana jako TRUTHY
    

print(bool(0))    # funkcja bool() sprawdza jaki stan prawda/fałsz ma zmienna albo doona wartość którą chcemy sprawdzić
print(bool(10))
print(bool(0.0))
print(bool(3.324))
print(bool(""))
print(bool("hello world"))