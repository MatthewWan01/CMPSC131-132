#Lab #2
#Due Date: 02/07/2020, 11:59PM
########################################
#                                      
# Name:Matthew Wan
# Collaboration Statement: discussed with Michael Grosman on calculations
# with real and imaginary numbers        
#
########################################

class VendingMachine:
    '''
        >>> x=VendingMachine()
        >>> x.purchase(215)
        'Machine out of stock'
        >>> x.deposit(10)
        'Machine out of stock. Take your $10 back'
        >>> x.restock(215, 9)
        'Invalid item'
        >>> x.newStock(215,2.50,9)
        'Current 215 stock: 9'
        >>> x.restock(215, 16)
        'Current item stock: 25'
        >>> x.newStock(156,3,3)
        'Current 156 stock: 3'
        >>> x.getStock()
        {215: [2.5, 25], 156: [3, 3]}
        >>> x.purchase(156)
        'Please deposit $3'
        >>> x.purchase(156, 2)
        'Please deposit $6'
        >>> x.purchase(156, 4)
        'Current 156 stock: 3'
        >>> x.deposit(2)
        'Balance: $2'
        >>> x.purchase(156)
        'Please deposit $1'
        >>> x.purchase(156, 2)
        'Please deposit $4'
        >>> x.deposit(5)
        'Balance: $7'
        >>> x.purchase(156)
        'Item dispensed, take your $4'
        >>> x.getStock()
        {215: [2.5, 25], 156: [3, 2]}
        >>> x.purchase(156)
        'Please deposit $3'
        >>> x.deposit(6)
        'Balance: $6'
        >>> x.purchase(156,2)
        'Item dispensed'
        >>> x.purchase(156)
        'Item out of stock'
        >>> x.deposit(62.5)
        'Balance: $62.5'
        >>> x.purchase(215,25)
        'Item dispensed'
        >>> x.deposit(6)
        'Machine out of stock. Take your $6 back'
        >>> x.newStock(156,3,3)
        'Item already registered'
        >>> x.restock(85, 10)
        'Invalid item'
    '''
    def __init__(self):
        #--- YOUR CODE STARTS HERE

        #Create profile
        self.balence = 0
        self.stock = {}

    def purchase(self, item, qty=1):
        #--- YOUR CODE STARTS HERE

        #Check if vending machine has anything
        if self.getStock() == {}:
            
            return 'Machine out of stock'

        #Check if select item is available 
        if self.stock.get(item) == None:
            
            return 'Invalid Item'

        #Item found    
        elif self.stock.get(item) != None:
            
            value = self.stock.get(item)

            #Check quantity of item
            if value[1] == 0:
                
                return 'Item out of stock'

            #See if take more than in store
            if qty > value[1]:
                
                return "Current " + str(item) + ' stock: ' + str(value[1])
            
            else:

                #Price
                debt = qty * value[0]

                #Under
                if debt > self.balence:
                    
                    return 'Please deposit $' + str(debt - self.balence)

                #Over
                if self.balence > debt:
                    
                    change = self.balence - debt
                    self.balence = 0
                    value[1] -= qty
                    return 'Item dispensed, take your $' + str(change)

                #Equal
                if self.balence == debt:
                    
                    value[1] -= qty
                    self.balence = 0
                    return 'Item dispensed'

    def deposit(self, amount):
        #--- YOUR CODE STARTS HERE

        #Check Types
        if (type(amount) == int or float):

            #change balence
            self.balence += amount
            tempBalence = self.balence
            j = 0 

            #Check items in stock
            for i in self.stock:
                value = self.stock.get(i)
                j += value[1]

            #Nothing in stock    
            if j == 0:
                
                self.balence = 0
                return 'Machine out of stock. Take your $' +  str(tempBalence) + ' back'  

            #Something in stock
            else:    
          
                return 'Balance: $' + str(self.balence)       
        

    def restock(self, item, stock):
        #--- YOUR CODE STARTS HERE

        #type check/item is registered
        if type(stock) == int and self.stock.get(item) != None:
            
            value = self.stock.get(item)
            value[1] += stock
            self.stock.update({item: value})
            
            return 'Current item stock: ' + str(value[1])

        #item no registered
        return 'Invalid item'

    def newStock(self, item, price, stock):
        #--- YOUR CODE STARTS HERE

        #type check/if item is regestered
        if (type(price) == int or float) and type(stock) == int:
            
            if self.stock.get(item) != None:
                
                return "Item already registered"

            #item not registered
            else:
            
                self.stock.setdefault(item, [price, stock])
            
                
        
                return 'Current ' + str(item) + ' stock: ' + str(stock)
      

    def getStock(self):
        #--- YOUR CODE STARTS HERE
        if self.stock == None:
            
            return 'Machine out of stock'
        
        return self.stock
    
class Complex:
    '''
        >>> a=Complex(5.2,-6)
        >>> b=Complex(2,14)
        >>> a+b
        (7.2, 8i)
        >>> a-b
        (3.2, -20i)
        >>> a*b
        (94.4, 60.8i)
        >>> a/b
        (-0.368, -0.424i)
        >>> b*5
        (10, 70i)
        >>> 5*b
        (10, 70i)
        >>> 5+a
        (10.2, -6i)
        >>> a+5
        (10.2, -6i)
        >>> 5-b
        (3, -14i)
        >>> b-5
        (-3, 14i)
        >>> print(a)
        5.2-6i
        >>> print(b)
        2+14i
        >>> b
        (2, 14i)
        >>> isinstance(a+b, Complex)
        True
        >>> a.conjugate
        (5.2, 6i)
        >>> b.conjugate
        (2, -14i)
        >>> b==Complex(2,14)
        True
        >>> a==b
        False
    '''
    def __init__(self, real, imag):
        # You are not allowed to modify the constructor
        self.real = real
        self.imag = imag
    
    #--- YOUR CODE STARTS HERE
    def __str__ (self):

        #if imag is +
        if self.imag > 0:
        
            return '{}+{}i'.format(self.real, self.imag)

        #if  imag is -
        return '{}{}i'.format(self.real, self.imag)
    
    def __repr__ (self):
        
        return '({}, {}i)'.format(self.real, self.imag)

    @property
    def conjugate (self):

        #multiple imag by -1
        return Complex(self.real, self.imag *-1)

    def __eq__(self,other):
        
        #Check if reals and imags are equals
        if (self.real == other.real) and (self.imag == other.imag):

            return True

        else:
            
            return False
    
    def __add__(self, other):
        
        #Add reals and add imags
        R = self.real + other.real
        I = self.imag + other.imag
        
        return Complex(R, I)

    def __radd__(self, other):

        #Add reals and add imags
        R = self.real + other.real
        I = self.imag + other.imag
        
        return Complex(R, I)
    
    def __sub__(self, other):

        #Sub reals and sub imags
        R = self.real - other.real
        I = self.imag - other.imag
        return Complex(R, I)
    
    def __rsub__(self, other):

        #Sub reals and sub imags
        R = other.real - self.real
        I = other.imag - self.imag
        return Complex(R, I)
    
    def __mul__(self, other):

        #Mul reals and Mul imags
        R = (self.real * other.real) - (self.imag * other. imag)
        I = (self.real * other.imag) + (self.imag * other.real)
        return Complex(R,I)
    
    def __rmul__(self, other):

        #Mul reals and Mul imags
        R = (self.real * other.real) - (self.imag * other. imag)
        I = (self.real * other.imag) + (self.imag * other.real)
        return Complex(R,I)
    
    def __truediv__(self, other):

        #Div two complexs
        first = complex(self.real, self.imag)
        second = complex(other.real, other.imag)
        result = first/second
        
        return Complex(result.real, result.imag)
        
