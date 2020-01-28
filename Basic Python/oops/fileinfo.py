import os
import time
class FileInfo:
          def __init__(self,filename):
                    self.filename=filename
                    self.f = open(self.filename,"r")
                    self.lines = self.f.readlines()
          def getlinecount(self):
                    print(len(self.lines))
          def getsize(self):
                    print(os.path.getsize(self.filename),"bytes")
          def getage(self):
                    age = time.time() - os.path.getctime(self.filename)
                    print(round(age/60/60/24),"days")
          def getfirstline(self):
                    self.getnthline(1)
          def getnthline(self,lineno):
                    print(self.lines[lineno-1].rstrip())
          def getlastline(self):
                    self.getnthline(0)
          def search(self,searchstring):
                    for lineno,line in enumerate(self.lines):
                              if searchstring in line:
                                        print(lineno+1,line.rstrip())
          def close(self):
                    self.f.close()
