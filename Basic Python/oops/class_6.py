class Test:
    def __init__(self):
        self.y=5
        z=10 #this is local to that function
    def printTest(self):
        print ('Test')
        print ("Value in print Test method:",self.y)
        print(self.z)
            
x=Test()
print( x.y)

x.printTest()

