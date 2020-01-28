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
class Stag():

    def __init__(self):
        print("Stag is ready")

    def whoisThis(self):
        print("Child - Stag")

    def run(self):
        print("Stag Runs faster")

    
class Fawn(Deer,Stag):
    def whoisThis(self):
        print("Fawn")
    def color(self):
        print("Its light brown color")
    

reed = Fawn()
reed.whoisThis()
reed.jump()
reed.run()
reed.color()
