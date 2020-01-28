from threading import Thread
from time import sleep,time
f=open("a.txt","r")
fout=open("b.txt","w")

def word(fin,fout):
	line = fin.readline()
	while line:
		fout.write(line)
		line = fin.readline()

start = time()
word(f,fout)
end = time()
print end - start

f.close()
fout.close()
