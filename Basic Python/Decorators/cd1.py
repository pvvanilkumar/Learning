#Decorator used on Class methods
def compare_name(method):
    def inner(name_ref):   #by default we have one argument in our method so pass one arg
        if name_ref.name=='Ujwal':
            print("Hello my name is also same")
        else:
            method(name_ref)
    return inner



class Printname:
    def __init__(self,name):
        self.name=name
    @compare_name
    def print_name(self):
        print("Hey you entered ",self.name)

pn=Printname('Ujwal')
pn.print_name()
