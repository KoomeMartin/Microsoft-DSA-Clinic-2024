# I will try to implement a fixed size circular queue which tracks the number of elements in the queue
# and adjust accordingly to each enqueued element 

class CircularQueue():
    def __init__(self,max_size):
        self.queue=[None] * max_size  # fixed size list
        self.front=-1 #pointer to the front part of the list
        self.rear=-1   #pointer to the rear part of the list
        self.max_size=max_size
    
    def is_empty(self):  #if pointer to front part remains as -1 the queue is still empty
        return self.front == -1
    
    def is_full(self):  #list is full if after circulating the rear part it equals the front part pointer
        return (self.rear + 1) % self.max_size == self.front
    
    def enqueue(self,data):
        if self.is_full():
            print('The queue is currently full!')
            return None
            
        if self.is_empty(): #if the queue is empty initialize the pointer to zero
            self.front=0
            
        self.rear=(self.rear + 1) % self.max_size # we are adding elements at the rear part , make it circular
        self.queue[self.rear] = data
        print(f'Equeued {data} to the queue')
    def dequeue(self):
        if self.is_empty():
            print('Cannot dequeue the queue is empty!')
            return None
        removed_item=self.queue[self.front]
        if self.front ==self.rear:  # if all the elements have been dequeued reset the pointer 
            self.front=-1
            self.rear =-1
        else:  #since we dequeue elements in the front part of the list we make front circular
            self.front= (self.front + 1) % self.max_size
            print(f'Dequeued {removed_item} from the queue')
            
    def peek(self):
        first_element=self.queue[self.front]
        print(f'The first element in the queue : {first_element}')
        
    def display(self):
        if self.rear >= self.front:
            print(f'Current queue: {self.queue[self.front:self.rear +1]}')
        else:
            print(f'Current queue: {self.queue[self.front:] } + {self.queue[:self.rear +1]}')
        

circular_queue=CircularQueue(4)

circular_queue.enqueue(90)
circular_queue.enqueue(40)
circular_queue.enqueue(60)
circular_queue.enqueue(10)
circular_queue.enqueue(100)
circular_queue.enqueue(900)


circular_queue.display()   

circular_queue.dequeue()

circular_queue.display()

circular_queue.enqueue(900)
        
circular_queue.display()  

circular_queue.dequeue()   

circular_queue.display()  

circular_queue.peek()
        