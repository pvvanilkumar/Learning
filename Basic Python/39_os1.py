#The OS module in python provides functions for interacting with the operating system. 
# This module provides a portable way of using operating system dependent functionality. 
#The *os* and *os.path* modules include many functions to interact with the file system.


import os
print(os.name) # gives the name of the operating system dependent module
print(os.getcwd())
os.chdir('C:\\Users') #works on windows
#os.chdir('C:/Users/')#works on unix and windows
print(os.getcwd())
