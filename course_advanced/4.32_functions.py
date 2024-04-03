def prints_four():
    print("this")
    print("is")
    print("an")
    print("example")

prints_four()
prints_four()
prints_four()
prints_four()


def function_name(parameter):  # defnicja funkcji zaczyna się od słowa "def" następnie "nazwa funkcji" zakończona "(tu podajemy parametry):"
    print(parameter +2)        # kod wykonywany w funkcji
                               # na końcu pozostawiamy 2 linie puste

function_name(10)      # wywołanie funkcji w kodzie


first_str = "The number "


def function_name(p1, p2, p3):
    print(p1 + str(p2) + p3)


function_name(first_str, 5, " is an integer.")


def default_example(num1=7, num2=8):
    print(num1 * num2)


default_example()
default_example(2)
default_example(5, 4)


def default_example2(num1=7, num2=8):
    return num1 * num2

product = default_example2(2)


def default_example3(num1=7, num2=8):
    return num1 * num2

print(default_example2() + 44)