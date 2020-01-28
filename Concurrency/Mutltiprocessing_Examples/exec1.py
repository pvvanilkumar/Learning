#exec() function is used for the dynamic execution of Python program which
#can either be a string or object code.
from math import *
s='print("Difference of 90 and 80 is",(90-80))'
exec(s)

#To check the function that exec()supports
exec('print(dir())')

# Except factorial all other math modules to be restricted 
exec("print(factorial(5))", {"factorial":factorial})

# factorial() renamed as fact 
exec('print(fact(5))', {'fact': factorial}) 

'''# An exception will be raised
exec("print(factorial(5))", {}) 
'''
