#class inheritance

class Employee(object): # base class
        """this is the base Employee class"""
        code="Emp"
        def __init__(self,id,name,mobile): # constructor
                self.id=id
                self.name=name
                self.mobile=mobile
        def get_mobile(self):
                """This functions print(s the mobile#"""
                print( self.mobile )
        def get_salary(self,days):
                return 1000*days
        def set_mobile(self,mobile):
                self.mobile=mobile
                        
class Trainee(Employee):#derived class
        code="Trainee"
        def get_salary(self,days):
                return 100*days
        def emp_salary(self,days): #for clarifying super
                print( super(Trainee,self).get_salary(days) )
        

laxmi=Trainee('223','Lakshmi','9866611005')#create a new Trainee
ujwal=Trainee('224','Ujwal','9848791790')#create a new Employee
laxmi.get_mobile()
laxmi.set_mobile('9440924316')
laxmi.get_mobile()
print( laxmi.get_salary(3) )
#print( type(laxmi)
print( " ******Employee Salary *********" )
ujwal.set_mobile("9573004499")
ujwal.get_mobile()
ujwal.emp_salary(5)


#python does not support function overloading ....it identifies with the name but not with the arguments

#whenever u use super u can see the overriden methods of u rparent
#multiple inheritance





