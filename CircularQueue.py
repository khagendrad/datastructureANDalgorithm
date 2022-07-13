# It is the extended version of regular queue, which solves major limitation of regular queue.
class CircularQ:
    def __init__(self, k):
        self.k = k 
        self.queue = [None]*k
        self.head = self.tail = 1 

    def enq(self, data):
        if ((self.tail+1)% self.k ==self.head):
            print("the circular queue is full\n")
        elif( self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail]=data 
        else:
            self.tail = (self.tail+1)% self.k
            self.queue[self.tail]=data

    def deq(self):
        if(self.head ==-1):
            print("The circular q is empty!\n")
        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp 
        else:
            temp = self.queue[self.head]
            self.head = (self.head+1)% self.k
            print(temp )
    
    def printQ(self):
        if self.head == -1:
            print("No element in the circular queue")
        
        elif self.tail>= self.head:
            for i in range(self.head, self.tail+1):
                print(self.queue[i], end=',')
                
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=',')
            for i in range(0, self.tail+1):
                print(self.queue[i], end=',')
            

cq = CircularQ(5)
cq.enq(1)
cq.enq(2)
cq.enq(3)
cq.enq(4)
cq.enq(5)
print("before deq:")
cq.printQ()
# cq.deq()
cq.deq()
print('\nafter dequeue:')
cq.printQ()
        