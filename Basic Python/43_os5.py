
import os
import time
print('File         :', __file__)   # refers to the current file
print('Created time  :', time.ctime(os.path.getctime(__file__)))
print('Access time  :', time.ctime(os.path.getatime(__file__)))
print('Modified time:', time.ctime(os.path.getmtime(__file__)))
print('Size         :', os.path.getsize(__file__))
print('test')
