#Multiple decorators on single function
def str_upper(func):
    def inner():
        str1= func()
        return str1.upper()
    return inner
def str_split(func):
    def wrapper():
        str2=func()
        return str2.split()
    return wrapper  

@str_split     #will be applied after str_upper is done
@str_upper     #will be applied first on the decorator

def print_str():
    return "good morning hyderabad"


print(print_str())
#Cant interchange upper and split as you cant use upper on list
