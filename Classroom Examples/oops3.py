#inheritance

class Dog:
	def speak(self):
		print("bhou..bhou")
	
tommy = Dog()
tommy.speak()

class GuardDog(Dog):
	def guard(self):
		print("I am guarding your home")

tiger = GuardDog()
tiger.speak()
tiger.guard()