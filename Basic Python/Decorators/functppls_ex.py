def wrap_ex(func):
    def inner():
        str1=func()
        return str1.upper()
    return inner
@wrap_ex
def greet():
    return "Hello Hyderabad"

print(greet)
print(greet.__name__)
# it gives the name as inner but the name is greet
#decorators hide some data of the original function
#if you want the original function name
#import functools
#before nested function add @functools.wraps(func)
#this is the decorator it will copy the lost data from the undecorated function or
#or the original function to the decorator closure .
#now it will print the original function name
'''import functools
def wrap_ex(func):
    @functools.wraps(func)
    def inner():
        str1=func()
        return str1.upper()
    return inner
@wrap_ex
def greet():
    return "Hello Hyderabad"

print(greet())
print(greet.__name__)'''
