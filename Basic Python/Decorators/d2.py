#using decorators
def str_upper(func):
    def inner():
        str1= func()
        return str1.upper()
    return inner
@str_upper
def print_str():
    return "good morning hyderabad"


print(print_str())
#d=str_upper(print_str)   #replacing the statement with decorator
#print(d())
