#applying class decorator on more than one function
class Check_div:
    def __init__(self,func):
        self.func=func
    def __call__(self,*args):
        list1=args[1:]
        for i in list1:
            if args[1]==0:
                return "Number canot be divided by zero"
            else:
                return self.func(*args)
@Check_div
def div(a,b):
    return a/b
def div1(a,b,c):
    return a/b/c
print(div(10,20))
print(div1(100,10,2))


