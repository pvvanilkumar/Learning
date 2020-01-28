class Car:
	def __init__(self,seats):
		self.seats=seats
	def __str__(self):
		return f"I am a {self.seats} seater car"
	def __len__(self):
		return self.seats
	def __add__(self,other):
		return self.seats + other.seats
	def __gt__(self,other):
		return self.seats > other.seats


innova = Car(7)
i10=Car(5)


print(i10)
print(innova)

print(len(i10))
print(len(innova))

print(i10 + innova)

print( i10 > innova )
