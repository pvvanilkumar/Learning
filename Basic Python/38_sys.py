import sys
print("Length:",len(sys.argv))
if (len(sys.argv)>2):
	sum=0
	for i in sys.argv[1:]:
		sum=sum+int(i)
	print(sum)
else:
        total=0
        no_Values=int(input("How many values has to be added:"))
        for val in range(no_Values):
                print(val)
                num=int(input("Enter Value:"))
                total+=num
        print(total)



