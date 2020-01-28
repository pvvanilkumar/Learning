import csv
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = "Marks"


f=open("marks.csv","r")

reader = csv.reader(f)

for row in reader:
	ws.append(row)
f.close()

wb.save("marks.xlsx")