#Lab #7
#Due Date: 04/24/2020, 11:59PM
########################################
#                                      
# Name:Matthew Wan
# Collaboration Statement:             
# Discussed with Michael Grossman on deleteMax on whether to use recursion 
########################################

class MaxPriorityQueue:
    '''
        >>> h = MaxPriorityQueue()
        >>> h.insert(10)
        >>> h.insert(5)
        >>> h.heap
        [10, 5]
        >>> h.insert(14)
        >>> h.heap
        [14, 5, 10]
        >>> h.insert(9)
        >>> h.heap
        [14, 9, 10, 5]
        >>> h.insert(2)
        >>> h.heap
        [14, 9, 10, 5, 2]
        >>> h.insert(11)
        >>> h.heap
        [14, 9, 11, 5, 2, 10]
        >>> h.insert(6)
        >>> h.heap
        [14, 9, 11, 5, 2, 10, 6]
        >>> h.parent(2)
        14
        >>> h.leftChild(1)
        9
        >>> h.rightChild(1)
        11
        >>> h.deleteMax()
        14
        >>> h.heap
        [11, 9, 10, 5, 2, 6]
        >>> h.deleteMax()
        11
        >>> h.heap
        [10, 9, 6, 5, 2]
        >>> x = MaxPriorityQueue()
        >>> x.insert(2)
        >>> x.insert(7)
        >>> x.deleteMax()
        7
        >>> x.insert(10)
        >>> x.insert(8)
        >>> x.insert(12)
        >>> x.deleteMax()
        12
        >>> x.insert(5)
        >>> x.insert(18)
        >>> x.heap
        [18, 10, 8, 2, 5]
    '''

    def __init__(self):
        self.heap=[]

    def __str__(self):
        return f'{self.heap}'

    __repr__=__str__

    def __len__(self):
        # YOUR CODE STARTS HERE
        return len(self.heap)


    def parent(self,index):
        # YOUR CODE STARTS HERE
        if len(self) <= 1 or index <= 1 or index > len(self): #if index out of bounds, one or less element, first index
            
            return None 
        
        else: #use float to find parent
            
            return self.heap[(index//2) - 1]

    def leftChild(self,index):
        # YOUR CODE STARTS HERE
        if len(self) <= 1 or index < 1 or index > len(self): #if index out of bounds, one or less element, first index
            
            return None 
        
        else:
            
            if index * 2 >= len(self): #leftChild does not exist
                
                return None
            
            return self.heap[(index*2)-1]

    def rightChild(self,index):
        # YOUR CODE STARTS HERE
        
        if len(self) <= 1 or index < 1 or index > len(self): #if index out of bounds, one or less element, first index
            
            return None 
        
        else:
            
            if index * 2 >= len(self): #rightChild doesnt exist
                
                return None
            
            return self.heap[(index*2)]

        

    def insert(self,x):
        # YOUR CODE STARTS HERE
        if len(self) == 0: #empty list
            
            self.heap.append(x)
            return
        
        else:
            
            self.heap.append(x) #add item to end
            index = len(self)
            
            while index > 1 and x > self.parent(index): #while x is greater than its parent, swap
                
                temp = self.parent(index)
                self.heap[self.heap.index(temp)] = x
                self.heap[index - 1] = temp
                index = index // 2
        
    
    def deleteMax(self):
        if len(self)==0:
            return None        
        elif len(self)==1:
            outMax=self.heap[0]
            self.heap=[]
            return outMax
    
        # YOUR CODE STARTS HERE
        
        temp = self.heap[0] #store delted item
        
        self.heap.pop(0) #move last item to first in list
        move = self.heap.pop(len(self)-1)
        self.heap.insert(0,move)
        
        if len(self.heap) == 2:
                
            if self.heap[0] >= self.heap[1]: #swap if left greater than right
                
                self.heap[0],self.heap[1] = self.heap[1],self.heap[0]
                return temp
            
            elif self.heap[1] >= self.heap[0]: #right greater than left
                
                self.heap[1],self.heap[0] = self.heap[0],self.heap[1]
                return temp
        
        
        
        index = 1
        while self.rightChild(index) != None: # has right
                
            if self.leftChild(index) != None: #has left
                
                if self.rightChild(index) >= self.leftChild(index): #right greater left
                    
                    if self.rightChild(index) <= move: #less than test value
                        
                        break
                    
                    else:
                        
                        self.heap[index-1], self.heap[index*2] = self.heap[index*2],self.heap[index-1] #swap places
                        index =index*2+1
                        
                elif self.leftChild(index) > self.rightChild(index): #left greater than right
                    
                    if self.leftChild(index) <= move: #left is smaller than value
                        
                        break
                    
                    else: #left is greater
                        
                        self.heap[index-1], self.heap[index*2-1] = self.heap[index*2-1],self.heap[index-1]
                        index = index*2
                        
            else: #no left
                
                if self.rightChild(index) <= move: #right less value
                    
                    break
                
                else: #right greater
                    
                    self.heap[index-1], self.heap[index*2-1] = self.heap[index*2-1], self.heap[index-1]
                    index = index*2 
        
        return temp