import os
import glob
os.mkdir('newDir')     #creating a new directory
os.rename('newDir','newDir1')   #rename directory

os.rmdir('newDir1')   #removing directory
os.chdir('C://')      #changing directory
print(os.getcwd())    #get current working directory


