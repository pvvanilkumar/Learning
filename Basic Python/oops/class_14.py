class Employee:
    company="TCS"
    def __init__(self,id,name,mobile): # constructor
        self.id=id
        self.name=name
        self.mobile=mobile
    def get_mobile(self):
        print( self.mobile )
    def set_mobile(self,mobile):
        self.mobile=mobile
    def company_name(self):
        print( "Company Name: ",self.company )
        self.company="Infosys"
        print( "Company Name after changing: ",self.company )
            
		
laxmi=Employee('257','Lakshmi','9866611005')#create a new employee
laxmi.get_mobile()
laxmi.set_mobile('9848791790')
laxmi.get_mobile()
print( type(laxmi) )
print( "laxmi.company:",laxmi.company )
print( Employee.company )
print( " ********************" )
laxmi.company_name() 
