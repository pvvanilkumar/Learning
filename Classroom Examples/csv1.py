import csv
f=open("marks.csv","r")

reader = csv.reader(f)

for row in reader:
	print(row[])
f.close()