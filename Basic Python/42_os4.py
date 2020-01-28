import os
path='C:/Users/admin/Desktop/PythonTutorials'

#Command to list all the files and directories
files=os.listdir(path)

#Prints all the files and directories
for file in files:
	print(file)
