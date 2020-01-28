#Using threads allows a program to run multiple operations concurrently
#in the same process space.

import threading
def worker():
    """thread worker function"""
    print('Worker')


threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()     #start is used to instantiate it with a target function


