import Queue

q = Queue.Queue()

#put items at the end of the queue
for x in range(4):
   q.put("item-" + str(x))

#remove items from the head of the queue
while not q.empty():
   print (q.get())