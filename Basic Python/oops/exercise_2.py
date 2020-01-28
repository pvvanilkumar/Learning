class Hero(object):
    def __init__(self,name):
        self.name=name
        self.health=100
    def eat(self,food):
        if (food=="apple"):
            self.health +=20 #self.health=self.health+20
        elif(food=='pizza'):
            self.health -=10
hb1=Hero("Sarat")
print (hb1.name)
print (hb1.health)
hb1.eat('apple')
hb2=Hero("Balu")

print ("After eating Apple : ",hb1.health)
hb2.eat('pizza')
print ("After eating Pizza: ",hb2.health)

