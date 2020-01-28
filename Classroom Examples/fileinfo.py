import os
import time
class FileInfo:
	def __init__(self,filename):
		self.filename=filename
		self.f = open(filename,'r')
		self.lines = self.f.readlines()
	def getsize(self):
		print(os.path.getsize(self.filename))
	def getnthline(self,lineno):print(self.lines[lineno-1])
	def firstline(self):self.getnthline(1)
	def lastline(self):self.getnthline(0)
	def age(self):
		now = time.time()
		created_time = os.path.getctime(self.filename)
		print(now - created_time)
	def linecount(self):
		print(len(self.lines))
	def close(self):
		self.f.close()