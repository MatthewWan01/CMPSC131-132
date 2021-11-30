#Lab #3
#Due Date: 02/21/2020, 11:59PM 
########################################
#                                      
# Name: Matthew Wan
# Collaboration Statement: discussed with Michael Grosman on how to formulate             
# a recursion state. Used online sourses to see how to move through a lst without
# assigning a variable 
########################################

'''
    REMINDER: All functions should not contain any for or while loops, or global variables. 
    Use recursion otherwise, no credit will be given
'''

def thirtyTwos(n, i=0):
    '''
        >>> thirtyTwos(432601)
        1
        >>> thirtyTwos(132432601)
        2
        >>> thirtyTwos(78)
        0
    '''
    ## YOUR CODE STARTS HERE
    if type(n) == int: #check type
        
        firstDigit = 0
        secondDigit = 0
        
        if n < 31: #final case
            
            return i
        
        if n > 31: #recursive case
            
            firstDigit = n // (10**(len(str(n)) - 1))
            secondDigit = (n - (firstDigit * (10**(len(str(n)) - 1)))) // (10**(len(str(n)) - 2))
           
            if (firstDigit == 3) and (secondDigit == 2): #test if 32    
                
               i += 1 
               
            return thirtyTwos(n - (firstDigit * (10**(len(str(n)) - 1))), i) #repeat without first digit of origonal number   


def flat(aList):
    '''
        >>> x = [3, [[5, 2]], 6, [4]]
        >>> flat(x)
        [3, 5, 2, 6, 4]
        >>> x
        [3, [[5, 2]], 6, [4]]
        >>> flat([1, 2, 3])
        [1, 2, 3]
        >>> flat([1, [], 3])
        [1, 3]
    '''
    ## YOUR CODE STARTS HERE      
    if [] in aList: #test for empty list
        
        aList.remove([])
    
    if len(aList) == 1: #single item in list
        
        if type(aList[0]) == list: #call method if element is list
                
            result = flat(aList[0])
        
        else: #add element if not list
                
            result = aList
    
    elif type(aList[0]) == list: #list size > 1
        
        result = flat(aList[0]) + flat(aList[1:]) #add first element call method
        
    else: #not list element,  add and  call method again
        
        result = [aList[0]] + flat(aList[1:])
    
    return result


############# DO NOT modify the triangle(n) function in any way! 
def triangle(n):
    return recursiveTriangle(n, n)
###################
    
def recursiveTriangle(k, n):
    '''
        >>> recursiveTriangle(2,4)
        '  **\\n   *'
        >>> print(recursiveTriangle(2,4))
          **
           *
        >>> triangle(4)
        '****\\n ***\\n  **\\n   *'
        >>> print(triangle(4))
        ****
         ***
          **
           *
    '''
    ## YOUR CODE STARTS HERE
    
    if k > 1: #recursive case
    
        parts = (n-k)*" " + k*("*") + "\n"
        
        return parts + recursiveTriangle(k-1,n)
    
    if k == 1: #final case
        
        return (n-k)*" " + k*("*")


def isPrime(num, i=2):
    '''
        >>> isPrime(5)
        True
        >>> isPrime(1)
        False
        >>> isPrime(0)
        False
        >>> isPrime(85)
        False
        >>> isPrime(1019)
        True
        >>> isPrime(2654)
        False
    '''
    ## YOUR CODE STARTS HERE
    if num <= 1: #special case
        
        return False
        
    if num % i == 0: #not prime
        
        return False
    
    if (i == num - 1): #prime
        
        return True
    
    return isPrime(num, i+1)