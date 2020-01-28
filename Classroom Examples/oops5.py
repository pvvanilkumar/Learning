class Week:
	def __init__(self):
		self.data = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
	def get_day(self,number):
		print(self.data[number -1])
	def __getitem__(self,key):
		return self.data[key -1]
	def __setitem__(self,key,value):
		self.data[key-1] = value
	def __delitem__(self,key):
		self.data[key-1]=None

a=Week()
a.get_day(4)

print(a[1])
a[1]="Sunday"
print(a[1])
del a[2]






