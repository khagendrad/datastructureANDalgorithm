# queue follow the first-in-first-out rule.
# basic operations 
# enqueue
# dequeue 
# isempty 
# isfull
# peek

from hamcrest import none


class Queue:
    def __init__(self) -> None:
        self.queue = []

    def enqueue(self,item):
        self.queue.append(item)
    
    def dequ(self):
        if len(self.queue)<1:
            return None
        return self.queue.pop(0)
    
    def display(self):
        print(self.queue)
    
q = Queue()
q.enqueue(1) # first element entered inside the queue
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print("before dequeue")
q.display()
q.dequ() # first element left/removed from the queue
print('after dequeue')
q.display()