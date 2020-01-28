#__init__in parent and child
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
    
bucky = Stag()
bucky.whoisThis()
bucky.jump()
bucky.run()
