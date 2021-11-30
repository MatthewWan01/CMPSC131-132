#Lab #0
#Due Date: 01/17/2020, 11:59PM
########################################
#                                      
# Name: Matthew Wan
# Collaboration Statement: Michael Grosman discussed using type function            
#
########################################

def sumSquares(aList):

    if type(aList) == list:
        
        theSum = 0
    
        for i in range (1,len(aList)):

            if (type(aList[i]) == int) or (type(aList[i]) == float):
        
                if ((abs(aList[i] % 3) == 0)):

                    theSum = theSum + square(aList[i])
                

        return theSum

def square(x):
    
    y = x * x
    return y

print(sumSquares(5))
