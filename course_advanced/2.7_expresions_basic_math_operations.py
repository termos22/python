dodawanie_addition = 4 + 5 # tak zapisuje się dodawanie
odejmowanie_subtraction = 45 - 23 # a tak zapisuje się odejmowanie
dzielenie_division = 45 / 5 # to jest przykład dzielenia
mnozenie_multiplication = 3 * 8 # natomiast tak przedstawia sie mnożenie

potegowanie_exponentation = 4 ** 2 # przykład potęgowania, czyli 4^2=16
dzielenie_calkowite_floor_division = 16 // 5 # część całkowita z dzielenia, 16/5=3,2 czyli wynikiem będzie 3
dzielenie_z_reszta_modulo = 7 % 3 # reszta z dzielenia, 7/3=2 reszty 1, czyli wynikiem będzie 1

# assignment operators - operatory przypisania
add_assign = 5
add_assign += 7 # wynikiem tego kodu jest przypisanie zmiennej, wartości wynikającej z dodawania 5+7

# analogicznie występują pozostałe operatory przypisania
sub = 10
sub -= 5 # da nam wartość 5 dla zmiennej sub

mult = 10
mult *= 5 # przypisze wartość 10*5=50 zmiennej mult

div = 10
div /= 5 # przypisze wartość 10/5=2 zmiennej div

exp = 10
exp **=2 # da nam wartość 10^2=100 w zmiennej exp

floor = 10
floor //= 6 # wynikiem będzie część całkowita z dzielenia 10//16=1

mod = 10
mod %= 7 # wynikiem będzie reszta z dzielenia 10/7, czyli 3

# kolejność wykonywania działań
# () najpierw wykonywane są działania w nawiasach
# ** w drugiej kolejności wykonywane jest potęgowanie
# % / // * następnie wykonywane jest równorzędnie modulo, floor div, dzielenie i mnożenie
# + - na końcu wykonywane są dodawania i odejmowania

dzialanie1 = (9-7)*2**3+10%6//-1*2-1

print(dzialanie1)

dzialanie2 = 15 / 3 * 2 * 2 - (3 + 4)
print(dzialanie2)