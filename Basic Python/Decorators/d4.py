#decorator without parameter
'''def my_decorator():
    print("Inside my_decorator")
    def wrapper(say_hello):
        print("Inside wrapper function, before func is called")
        return say_hello()
        print("after func is called")
    return wrapper
@my_decorator()
def say_hello():
    print("Hello")
'''


#decorator with parameters

def decorator(*args, **kwargs):
    
    print("Inside decorator") 
    def inner(func1): 
        print("Inside inner function") 
        print("I like", kwargs['like'])
        for x in args:
            print("I also play {}".format(x))
        return func1 
    return inner 
  
@decorator('badminton','tennis',like = "cricket") 
def func1(): 
    print("Inside actual function") 
 
