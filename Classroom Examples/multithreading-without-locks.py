from threading import Thread
from time import sleep,time
f=open("a.txt","r")
fout=open("c.txt","w")

def word(fin,fout):
	line = fin.readline()
	while line:
		fout.write(line)
		line = fin.readline()
	
threads=[Thread(target=word,args=(f,fout)) for x in range(50)]
start = time()
for t in threads:t.start()
for t in threads:t.join()

end = time()
print end - start

f.close()
fout.close()
