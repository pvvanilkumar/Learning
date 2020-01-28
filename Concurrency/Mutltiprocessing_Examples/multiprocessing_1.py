import multiprocessing
#The simplest way to spawn a second process is to instantiate
#a Process object with a target function and call start()
#to let it begin working.


def worker(num):
    """worker function"""
    print('Worker',num)
    return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker,args=(i,))
        jobs.append(p)
        p.start()
        
    
