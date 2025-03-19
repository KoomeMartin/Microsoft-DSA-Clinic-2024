#we first create a class which will implement the stack absract data structure 
#it is a Last in First out data structure which allows push,pop,peek,is_empty operations 

class Stack():
    def __init__(self):
        self.stack=[]  # I will implement this stack using a python list
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self,data):
        self.stack.append(data)
        print(f'Pushed {data} to the stack')
        
    def pop(self):
        if not self.is_empty(): #check if stack is empty
            removed_item=self.stack.pop() #pop removes the last element in the list
            
            print(f'Removed {removed_item} from the stack')
        else:
            print('Can not pop an empty stack!')
    def peek(self):
        last_item=self.stack[-1]
        print(f'This is the last element in the stack {last_item} ')
        
    def print(self):
        print(f'Current stack structure: {self.stack}')
        

stack=Stack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

stack.print()
stack.pop()
stack.print()

stack.peek()
        