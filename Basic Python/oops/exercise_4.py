class Dog(object):
    def speak(self):
        print( "bhou..bhou" )
    def guard(self):
        print( "I am guarding your home" )

class Cat(object):
    def speak(self):
        print( "meau..meau" )
    def hunt(self):
        print( "I am hunting mice" )


class Dd(Dog):
    def hobby(self):
        print( "Biting" )
    def guard(self):
        print( "Guarding house" )
    def oldguard(self):
        super(Dd,self).guard()

ginger=Dd()
ginger.guard()
ginger.speak()
ginger.hobby()
ginger.oldguard()
print("*******************************************************")
class Doat(Cat,Dog):
    def hobby(self):
        print( "programming in python" )

    def speak(self):print( "bhou..meau" )
    def oldspeak(self):
        super(Doat,self).speak()
    
ginger1=Doat()
ginger1.speak()
ginger1.guard()
ginger1.hunt()
ginger1.hobby()
ginger1.oldspeak()


