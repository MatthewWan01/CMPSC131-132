#Lab #4
#Due Date: 03/06/2020, 11:59PM 
########################################
#                                      
# Name: Matthew Wan
# Collaboration Statement: Used online sources to see how to move through linked list         
#
########################################

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class SortedLinkedList:
    '''
        >>> x=SortedLinkedList()
        >>> x.pop()
        >>> x.add(8.76)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(5)
        >>> x.add(3)
        >>> x.pop()
        8.76
        >>> x.add(-7.5)
        >>> x.add(4)
        >>> x.add(9.78)
        >>> x.add(4)
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 1 1 1 3 4 4 5 9.78
    '''

    def __init__(self):   # You are not allowed to modify the constructor
        self.head=None
        self.tail=None
        self.count=0

    def __str__(self):   # You are not allowed to modify this method
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' '.join(out) 
        return ('Head:{}\nTail:{}\nList:{}'.format(self.head,self.tail,out))

    __repr__=__str__


    def isEmpty(self):
        # --- YOUR CODE STARTS HERE
        
        if (self.count == 0): 
            
            return True
        
        return False
    
    def __len__(self):
        # --- YOUR CODE STARTS HERE
        return self.count 
                
    def add(self, value):
        # --- YOUR CODE STARTS HERE
        
        node = Node(value) #create new node 
        
        if self.head is None or self.head.value >= node.value: #if no entries or if node is smaller than first entry
            node.next = self.head
            self.head = node
            self.tail = node
            self.count += 1
            return self.head
        
        temp = self.head
            
   
        current = self.head
        while current.next is not None and current.next.value < node.value: #if node isnt biggest or smallest node
            current = current.next
        node.next = current.next
        current.next = node
        self.count += 1
        
        
        while temp.next is not None:  #move through list to set tail
             
            temp = temp.next 
            
            self.tail = temp
            
        return self.head
        
    def pop(self):
        # --- YOUR CODE STARTS HERE
        if self.head == None or self.head.next == None: #check for entries or if only 1 entry
            
            return None
        
        temp = self.head
        
        while temp.next.next is not None: #get last entry
            
            temp = temp.next
        
        num = temp.next #remeber last entry
        self.tail = temp
        temp.next = None #remove last entry
        
        self.count -= 1
        
        return num.value #print entry removed
    
    # -- If you are attempting the extra credit, uncomment the method definition below

    def replicate(self):
        # --- YOUR CODE STARTS HERE
        nlist = SortedLinkedList()#new list
        
        temp = self.head
        
        while temp.next is not None: #move through origonal list
            
            nlist.add(temp.value) #add  value from origonal to new
            
            if temp.value > 0 and type(temp.value) == int: #check for positive integers
                
                for i in range(temp.value -1): #repeat for num - 1
                    
                    nlist.add(temp.value)
                
            temp = temp.next
            
        if temp.next is None: #if last node in list fits condition
            
            nlist.add(temp.value)
            
            if temp.value > 0 and type(temp.value) == int:
                
                for i in range(temp.value -1):
                    
                    nlist.add(temp.value)
                    
        return nlist