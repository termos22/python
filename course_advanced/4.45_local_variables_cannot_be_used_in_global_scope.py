# Local variables cannot be used by code in the global scope
def loc_ex():
    breakfast = "waffles"
    return breakfast


loc_ex()
print(breakfast)