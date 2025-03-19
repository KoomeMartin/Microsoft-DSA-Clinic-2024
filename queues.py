# I will implement a Queue abstract data type using a python list 
# I will try applying some functionalities in the queue ; enqueue,dequeue,peek,is_empty,limit size of list
# Queues are FIFO data structure (First in First out )

class Queue():
    def __init__(self,max_size):
        self.queue=[]
        self.max_size=max_size  #limit the size of the queue
        
    def is_empty(self):
        return len(self.queue) == 0
    def is_full(self):
        if len(self.queue) == self.max_size:
            print('The queue is currently full!')
        else:
            print(f'There is space available in the queue: {self.max_size-len(self.queue)} slots remaining')
    
    def enqueue(self,data):
        if len(self.queue) < self.max_size:
            self.queue.append(data)
            print(f'Enqueued {data} in the queue')
        else:
            print(f'Cannot enqueue {data}. Queue is full!')
            
    def dequeue(self):
        if not self.is_empty():
            removed_item=self.queue.pop(0) # remove the first element in the queue
            
            print(f'Dequeued {removed_item} from the queue ')
        else:
            print(f'The Queue is empty!')
            
    def peek(self):
        first_element=self.queue[0]
        print(f'The first element in the list is : {first_element}')
        
    def dispaly(self):
        print(f'Current queue: {self.queue}')
        

queue=Queue(4)
queue.enqueue(20)
queue.enqueue(10)
queue.enqueue(90)

queue.is_full()

queue.dispaly()
queue.dequeue()
queue.dispaly()

queue.peek()