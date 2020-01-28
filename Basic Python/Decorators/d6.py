#Passing parameter with decorators
def outer(city):
    def str_upper(func):
        def inner():
            return func() + city
        return inner
    return str_upper

@outer("Chennai")
def ordinary():
    return("Good Morning ")
print(ordinary())
