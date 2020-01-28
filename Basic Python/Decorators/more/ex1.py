def my_decorator():
    print("Inside my_decorator")
    def wrapper(say_hello):
        print("Inside wrapper function, before func is called")
        return say_hello()
        print("after func is called")
    return wrapper
@my_decorator()
def say_hello():
    print("Hello")


