#wrapping a function with another function
def str_upper(func):
    def inner():
        str1= func()
        return str1.upper()
    return inner
def print_str():
    return "good morning hyderabad"


print(print_str())
d=str_upper(print_str)
print(d())
