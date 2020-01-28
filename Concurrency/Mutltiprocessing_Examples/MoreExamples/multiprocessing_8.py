'''By default, the main program will not exit until all of the children have exited.
There are times when starting a background process that runs without blocking
the main program from exiting is useful, such as in services where there may
not be an easy way to interrupt the worker, or where letting it die in the
middle of its work does not lose or corrupt data.

To mark a process as a daemon, set its daemon attribute to True.
The default is for processes to not be daemons.'''
import multiprocessing
import time
import sys


def daemon():
    p = multiprocessing.current_process()
    print('Starting:', p.name, p.pid)
    sys.stdout.flush()
    time.sleep(2)
    print('Exiting :', p.name, p.pid)
    sys.stdout.flush()


def non_daemon():
    p = multiprocessing.current_process()
    print('Starting:', p.name, p.pid)
    sys.stdout.flush()
    print('Exiting :', p.name, p.pid)
    sys.stdout.flush()


if __name__ == '__main__':
    d = multiprocessing.Process(
        name='daemon',
        target=daemon,
    )
    d.daemon = True

    n = multiprocessing.Process(
        name='non-daemon',
        target=non_daemon,
    )
    n.daemon = False

    d.start()
    time.sleep(1)
    n.start()
