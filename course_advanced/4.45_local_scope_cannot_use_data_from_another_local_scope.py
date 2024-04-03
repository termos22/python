# The local scope of one function can:t usevariables
# from another function's local scope

def first():
    loc = 2
    return loc


def second():
    return loc


first()
second()
