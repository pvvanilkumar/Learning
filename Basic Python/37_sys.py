import sys
#print(len(sys.argv))
if (len(sys.argv)>1):
	sum=0
	for i in sys.argv[1:]:
		sum=sum+int(i)
	print("Sum of the values:",sum)
else:
	print ("Please give atleast two parameters")



