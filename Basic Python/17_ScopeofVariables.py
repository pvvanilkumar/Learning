#scope of variables

for x in range(10):
    x=x+2
print(x)

print("Before Function :",x)

def add(x):
    print("Inside the function:",x)
add(20)
print("After Function :",x)

def add1(): #if you are not passing the value it will take the global value
    print(x)
add1()
