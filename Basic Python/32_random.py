#random module
"""
Write a program to find the random numbers from 1 to 100 and call the function
for 500 times and print how many times each numbers has been repeated

"""

import random
def myrandom():
	return random.randint(1,100)
#2. Call the function 500 times and save the results into a list.
r=[]
for x in range(500):
	r.append(myrandom())

#3. Print how many times each number has repeated
for x in set(r):
	print( x,r.count(x))


