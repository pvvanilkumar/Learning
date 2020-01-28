from fileinfo import FileInfo
f = FileInfo("test.txt")
f.getsize()
f.firstline()
f.lastline()
f.age()
f.linecount()
f.close()