import os

child_pid = os.fork()
if child_pid != 0:
    print(os.waitpid(child_pid, 0))
