'''In a situation where separate code from the same thread needs to
're-acquire' the lock, use an RLock instead.
'''

import threading

lock = threading.RLock()

print('First try :', lock.acquire())
print('Second try:', lock.acquire(0))
