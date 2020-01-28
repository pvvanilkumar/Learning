#usage of super 
# parent class
class Deer:
    
    def __init__(self):
        print("Deer is in forest")

    def whoisThis(self):
        print("Parent - Deer")

    def jump(self):
        print("Deer is jumping")

# child class
class Stag(Deer):

    def __init__(self):
        print("Stag is ready")

    def whoisThis(self):
        print("Child - Stag")

    def run(self):
        print("Runs faster")

    def parentwhoisThis(self):
        #super(Stag,self).whoisThis()
        super().whoisThis()

bucky = Stag()
bucky.whoisThis()
bucky.jump()
bucky.run()
bucky.parentwhoisThis()
