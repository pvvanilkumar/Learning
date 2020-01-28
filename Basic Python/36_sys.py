#sys.argv - contains command line arguments
#from sys import argv
import sys
print(type(sys.argv))
script,first, second =sys.argv

print(len(sys.argv))
print("The script is called:",script)
print("The first variable is :",first)
print("Your Second variable is :", second)
