import sys
filename = sys.argv[1]
pattern  = sys.argv[2]

f=open(filename,"r")
for lineno,line in enumerate(f):
	if pattern.lower() in line.lower():
		print(lineno+1,line, end = "")
f.close()