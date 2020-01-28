import os
fpath1='C:/Users/admin/Desktop/PythonTutorials'
for (dirname, subdir, files) in os.walk(fpath1):
     #print("------",files)
     for myfile in files:
        filename=os.path.join(dirname,myfile)
        if filename.endswith(".txt"):
            print(filename)
