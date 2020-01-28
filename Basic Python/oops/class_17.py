class Dog(object):
    def speak(self):
        print ("Dog: ...............","bhou..bhou")
    def guard(self):
        print ("Dog: ...............","I am guarding your home")

class Cat(object):
    def speak(self):
        print ("Cat: ...............","meau..meau")
    def hunt(self):
        print ("Cat: ...............","I am hunting mice")

class Doat(Cat,Dog):
    def hobby(self):
        print ("Doat: ...............","programming in python")

    def speak(self):print ("Doat: ...............","bhou..meau")
    def oldspeak(self):
        super(Doat,self).speak()
    
ginger=Doat()
ginger.speak()
ginger.guard()
ginger.hunt()
ginger.hobby()
ginger.oldspeak()


