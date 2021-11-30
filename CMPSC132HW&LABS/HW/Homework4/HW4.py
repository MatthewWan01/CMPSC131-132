#HW4
#Due Date: 04/25/2020, 11:59PM EST 
########################################
#                                      
# Name: Matthew Wan
# Collaboration Statement:             
# Disccused with Kalp Patel and Michael grosman on put method
########################################

class ContentItem:
    def __init__(self, cid, size, header, content):
        self.cid = cid
        self.size = size
        self.header = header
        self.content = content

    def __str__(self):
        return ('CONTENT ID: {} SIZE: {} HEADER: {} CONTENT: {}'.format(self.cid, self.size, self.header, self.content))

    __repr__=__str__


class Node:
    def __init__(self, content):
        self.value = content
        self.next = None

    def __str__(self):
        return ('CONTENT:{}\n'.format(self.value))

    __repr__=__str__


class CacheList:
    def __init__(self, size):
        self.head = None
        self.tail = None
        self.maxSize = size
        self.remainingSize = size
        self.numItems = 0

    def __str__(self):
        listString = ""
        current = self.head
        while current is not None:
            listString += "[" + str(current.value) + "]\n"
            current = current.next
        return ('REMAINING SPACE:{}\nITEMS:{}\nLIST:\n{}\n'.format(self.remainingSize, self.numItems, listString))     

    __repr__=__str__

    def __len__(self):
        return self.numItems
    

    def put(self, content, evictionPolicy):
        # YOUR CODE STARTS HERE
        if self.maxSize >= content.size: #see if content size can fit
            
            node = Node(content) #create node
            
            if self.numItems == 0 and content.size <= self.remainingSize: #no items and fits
                self.head = node
                self.tail = node
                self.remainingSize -= content.size
                self.numItems += 1
                return "INSERTED: " + content.__str__()
            
            temp = self.head
            while temp.next != None: #traverse list
                if node.value.cid == temp.value.cid: #if content already in list
                    return "Insertion of content item " + str(node.value.cid) + "not allowed. Content already in cache."
                else:
                    temp = temp.next
            
            while self.remainingSize < content.size: #if not enough space
                if evictionPolicy == "mru":
                    self.mruEvict()
                if evictionPolicy == "lru":
                    self.lruEvict()
            
            node.next = self.head #add node to front
            self.head = node
            self.remainingSize -= content.size
            self.numItems += 1
            return "INSERTED: " + content.__str__()
        else:
            return "Insertion not allowed. Content size is too large."

    def find(self, cid):
        # YOUR CODE STARTS HERE
        temp = self.head
        prev = None
        
        while temp.next != None: #traverse the list
            if temp.value.cid == cid: #if the ids match, put node into front
                if prev != None:
                    prev.next = temp.next
                    self.head = temp
                return temp.__str__()
            else:
                prev = temp
                temp = temp.next
                
        return None

    def update(self, cid, content):
        # YOUR CODE STARTS HERE
        if self.find(cid) == None: #node not in list
            return None
        else: #node in list
            mContent = self.find(cid)
            mContent.content = content
            return "UPDATED CONTENT : " + mContent.__str__()
            
    def mruEvict(self):
        # YOUR CODE STARTS HERE
        if self.head == None: #no element
            self.tail == None
        else: #multiple elements
            remove = self.head
            self.head = remove.next
            self.remainingSize += remove.value.size
            self.numItems -= 1
            remove.next = None
    
    def lruEvict(self):
        # YOUR CODE STARTS HERE
        if self.head.next == None: #only 1 or less element
            self.remainingSize += self.head.value.size
            self.numItems -= 1
            self.head = None
            
        else: #more than 1 element
            temp = self.head
            while temp.next != None:
                if temp.next == self.tail:
                    self.remainingSize += temp.next.value.size
                    self.numItems -= 1
                    self.tail = temp
                    temp.next = None
                else:
                    temp = temp.next
    
    def clear(self):
        # YOUR CODE STARTS HERE      
        self.head = None #reset to default
        self.tail = None
        self.maxSize = 200
        self.remainingSize = 200
        self.numItems = 0
        return "Cleared Cache!"


class Cache:
    """
    A more comprehensive doctest is provided in the HW4_doctest.py file. 
    You can replace this doctest when you are ready to test your entire code
    
    >>> cache = Cache()
    >>> content1 = ContentItem(1000, 10, "Content-Type: 0", "0xA")
    >>> content2 = ContentItem(1003, 13, "Content-Type: 0", "0xD")
    >>> content3 = ContentItem(1008, 242, "Content-Type: 0", "0xF2")
    >>> cache.insert(content1, 'lru')
    'INSERTED: CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA'
    >>> cache.insert(content2, 'lru')
    'INSERTED: CONTENT ID: 1003 SIZE: 13 HEADER: Content-Type: 0 CONTENT: 0xD'
    >>> cache.insert(content3, 'lru')
    'Insertion not allowed. Content size is too large.'
    >>> cache
    L1 CACHE:
    REMAINING SPACE:177
    ITEMS:2
    LIST:
    [CONTENT ID: 1003 SIZE: 13 HEADER: Content-Type: 0 CONTENT: 0xD]
    [CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA]
    <BLANKLINE>
    <BLANKLINE>
    L2 CACHE:
    REMAINING SPACE:200
    ITEMS:0
    LIST:
    <BLANKLINE>
    <BLANKLINE>
    L3 CACHE:
    REMAINING SPACE:200
    ITEMS:0
    LIST:
    <BLANKLINE>
    <BLANKLINE>
    <BLANKLINE>
    """

    def __init__(self):
        self.hierarchy = [CacheList(200) for _ in range(3)]
        self.size = 3
    
    def __str__(self):
        return ('L1 CACHE:\n{}\nL2 CACHE:\n{}\nL3 CACHE:\n{}\n'.format(self.hierarchy[0], self.hierarchy[1], self.hierarchy[2]))
    
    __repr__=__str__

    def clear(self):
        for item in self.hierarchy:
            item.clear()
        return 'Cache cleared!'

    def hashFunc(self, contentHeader):
        # YOUR CODE STARTS HERE
        value = 0
        for i in contentHeader:#get ASCII Value for each character
            value += ord(i)
        return value % 3 #cache level
            

    def insert(self, content, evictionPolicy):
        # YOUR CODE STARTS HERE
        cache = self.hashFunc(content.header) #cache level
        return self.hierarchy[cache].put(content, evictionPolicy)


    def retrieveContent(self, content):
        # YOUR CODE STARTS HERE
        cache = self.hashFunc(content.header) #cache level
        if self.hierarchy[cache].find(content.cid) == None: #not in cache
            return "Cache Miss!"       
        return self.hierarchy[cache].find(content.cid)
        

    def updateContent(self, content):
        # YOUR CODE STARTS HERE
        cache = self.hashFunc(content.header) #cache level
        return self.hierarchy[cache].update(content.cid, content.content)
