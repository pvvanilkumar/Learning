marks = [
("sandeep",35,79,100),
("Rakesh",50,75,94),
("Suma",50,50,50),
("sashank",79,50,67)
]

print(sorted(marks))
print(sorted(marks,key=lambda x:x[0].lower()))
print(sorted(marks,key=lambda x:x[0][1]))
print(sorted(marks,key=lambda x:x[1]))
print(sorted(marks,key=lambda x:x[-1]))
print(sorted(marks,key=lambda x:sum(x[1:]),reverse=True))

