#Same decorator used on multiple functions

def div_decorator(func):
    def inner(*args):
        list1=args[1:]
        for i in list1:
            if i==0:
                return "Cannot divide number by zero"
        return func(*args)
    return inner
@div_decorator
def div1(a,b):
    return a/b
@div_decorator
def div2(a,b,c):
    return a/b/c

print(div1(40,3))
print(div2(100,5,2))
