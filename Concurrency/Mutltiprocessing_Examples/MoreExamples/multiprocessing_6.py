#Determining the current process
'''Each Process instance has a name with a default value that can be
changed as the process is created. Naming processes is useful for keeping track of them,
especially in applications with multiple types of processes running simultaneously.'''
import multiprocessing
import time
def worker():
    name = multiprocessing.current_process().name
    print(name, 'Starting')
    time.sleep(2)
    print(name, 'Exiting')

def my_service():
    name = multiprocessing.current_process().name
    print(name, 'Starting')
    time.sleep(3)
    print(name, 'Exiting')


if __name__ == '__main__':
    service = multiprocessing.Process(
        name='my_service',
        target=my_service,
    )
    worker_1 = multiprocessing.Process(
        name='worker',
        target=worker,
    )
    worker_2 = multiprocessing.Process(  # default name
        target=worker,
    )

    worker_1.start()
    worker_2.start()
    service.start()
