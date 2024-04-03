# Global variables can be accessed by code in a local scope.
def print_glob():
    loc_var = " this is very long."
    print(glob_var + loc_var)


glob_var = "This is a string"
print_glob()
