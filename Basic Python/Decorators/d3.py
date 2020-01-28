#decorator function with parameters
def div_decorator(func):
    def inner(x,y):
        if y==0:
            return "Cannot divide number by zero"
        return func(x,y)
    return inner
@div_decorator
def div(a,b):
    return a/b

print(div(5,10))
print(div(0,60))
print(div(10,0))
