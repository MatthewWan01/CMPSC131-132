#LAB 9
#Due Date: 04/11/2020, 11:59PM EST
########################################
#                                      
# Name: Matthew Wan
# Collaboration Statement:             
#Fixed discussed with Michael Grossman to fix delete max code
########################################

class MaxPriorityQueue:
    ### Copy and paste your code from LAB 7 here
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



def heapSort(numList):
    '''
       >>> heapSort([9,7,4,1,2,4,8,7,0,-1])
       [-1, 0, 1, 2, 4, 4, 7, 7, 8, 9]
    '''
    sortHeap = MaxPriorityQueue()
    # -- YOUR CODE STARTS HERE
    newHeap = []
    
    if type(numList) != list: #type check
        
        return None
    
    else:
    
        for i in numList:
            
            if type(i) == float or type(i) == int: #type check inseret into heap
                sortHeap.insert(i)
    
    while len(sortHeap) > 0: #go through all elements
    
        newHeap.insert(0, sortHeap.deleteMax()) #deleteMax and add to front
        
    return newHeap 