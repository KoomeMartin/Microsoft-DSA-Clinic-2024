
#Each element in a linked list is basically a node that contains data point a pointer to the next data point

class Node():  # create a node class
    def __init__(self,data):
        self.data=data   #data point in a node
        self.next=None   # pointer to the next data point 
        
class LinkedList():
    def __init__(self):
        self.head=None    # first element in the linked list
        
    def append(self,data):
        new_node=Node(data)
        
        if self.head is None:  # Check if head value exist and assign to a new node if not
            self.head=new_node    
        else:
            current=self.head   # If head exist  it is our current start data point
            while current.next:  # Loop through to the end of the list
                current = current.next
            current.next=new_node  #link the first node to the next node
            
    def print_list(self):  #print the linked list
        current = self.head
        while current:
            print(current.data , end=' -> ')
            current=current.next
        print(None)
        
    def reverse(self):
        previous= None  #reversing holder
        current = self.head
        while current:
            next_node=current.next #take note of the next node before reversing
            current.next = previous #reverse the pointer to the previous node 
            previous = current    #current node is already reversed
            current = next_node  #go to the next node in the original list and reverse pointer 
        self.head=previous  #assign head to the last previous assigned value
        
ll=LinkedList()
ll.append(7)
ll.append(9)
ll.append(0)

print('Linked list created')
ll.print_list()
print('You have reversed the linked lis')
ll.reverse()

ll.print_list()