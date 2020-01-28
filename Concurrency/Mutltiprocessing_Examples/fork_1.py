#fork is one of the method to start a process in python
'''The system function call fork() creates a copy of the process,
which has called it. This copy runs as a child process of the calling process.
The child process gets the data and the code of the parent process.''' 
import os
'''def child():
    n=os.fork()
    if n >0:
        print("Parent process PID :",os.getpid())
    else:
        print("Child process PID :",os.getpid())
child()'''
 
