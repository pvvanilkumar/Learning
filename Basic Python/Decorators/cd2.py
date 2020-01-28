#calling an object directly (__call__)
class Printname:
    def __init__(self,name):
        self.name=name
    
    def print_name(self):
        print("Hey you entered ",self.name)

pn=Printname('Ujwal')
pn.print_name()


'''
pn.pn_name() ...as the method is callable we are able call it
what if we want to call the object pn() instead of pn.method()
we get an error Type error object is not callable
so to make it callable 
we have an inbuilt method __call__
replace print_name with __call__ than u can call the object

'''
