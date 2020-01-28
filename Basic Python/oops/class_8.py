class Deer:
    def whoisThis(self):
        print("Parent - Deer" ) 
    def gender(self):
        print("Parent - Female")
class Child(Deer):
    def gender(self):
        print("Child - Male")

bucky=Child()
bucky.whoisThis()
bucky.gender()
