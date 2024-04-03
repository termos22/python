# comparison operators - operatory porównania
# 
#   >   - większe
#   <   - mniejsze
#   >=  - większe równe
#   <=  - mniejsze równe
#   !=  - różne (nie równe)
#   ==  - równe


print(4 > 2)
print(1 > 3)

print(5.79 < 6)
print(3 < 3)

print(9 >= 9)
print(1 <= 2)

print(10 != 100)
print(10 != 10)

print(10 == 100)
print(10 == 10)

print("hello" == "hello")
print("hello" != "world")
print("Hello" == "hello")

print(4.0 >= 4)
print(4.0 <= 4)
print(4.0 == 4)


# boolean operators - operatory logiczne (Boolowskie)
# 
#   and   - i 
#   or    - lub
#   not   - nie
# 
#    and   - tablica prawdy
# True and True    > True
# True and False   > False
# False and False  > True
# False and True   > True
print(4 > 1 and "word" == "word")    # True and True   -> True 
print(8.76 == 8.7600 and 2 != 2)     # True and False  -> False
print("earth" == "Earth" and 6 <= 3) # False and False -> False
print(10 == 5 and 10 != 5)           # False and True  -> False
# 
#    or    - tablica prawdy
# True or True    > True
# True or False   > True
# False or False  > False
# False or True   > True
print(4 > 1 or "word" == "word")    # True or True   -> True 
print(8.76 == 8.7600 or 2 != 2)     # True or False  -> True
print("earth" == "Earth" or 6 <= 3) # False or False -> False
print(10 == 5 or 10 != 5)           # False or True  -> True
# 
#    not    - tablica prawdy
# not True    > False
# not False   > True
print(not 6482 > 0)                # not True  -> False
print(not "Python" != "Python")    # not False -> True