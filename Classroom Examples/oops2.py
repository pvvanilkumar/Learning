#inheritance
#docstrings

class Dog:
	"""
	this is a 
	class
	dog
	"""
	def speak(self):
		"""
		this method helps
		the dog speak
		"""
		print("bhou..bhou")
	
tommy = Dog()
tommy.speak()
print(dir(tommy))
help(tommy.speak)
print(tommy.speak.__doc__)
