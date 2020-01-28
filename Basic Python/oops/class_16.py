class Baby(object):
	babycount=0 # class variable
	def __init__(self,nickname):
		self.nickname=nickname
		#Baby.babycount =Baby.babycount+1
		#Baby.babycount +=1
	def cry(self):
		print( "Baby {} is crying :(( .......".format(self.nickname))
	def laugh(self):
		print ("Baby {} is laughing Ha ha ha : ))".format(self.nickname))
	
baby1=Baby('Pinky')
baby2=Baby('Munna')

baby1.cry()
baby2.laugh()

print (Baby.babycount)
