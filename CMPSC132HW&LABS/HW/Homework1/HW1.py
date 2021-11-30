#HW #1
#Due Date: 01/31/2020, 11:59PM 
########################################
#                                      
# Name:
# Collaboration Statement:             
#
########################################

# Don't forget to remove testing code that is outside of the functions, including any input() calls
import math
import string

def rectangle(perimeter,area):
    """
        >>> rectangle(14, 10) # From a 2x5 rectangle
        5
        >>> rectangle(12, 5) # From a 1x5 rectangle
        5
        >>> rectangle(25, 25) # A 2.5x10, but one side is not an integer
        >>> rectangle(50, 100) # From a 5x20 rectangle
        20
        >>> rectangle(11, 5)
        >>> rectangle(11, 4)
    """
    # --- YOU CODE STARTS HERE
    sidesqrt = (math.sqrt((perimeter**2) - (16*area)))
    bigSide  = (perimeter + sidesqrt)/4
    smallSide = (perimeter - sidesqrt)/4
    if (bigSide % 1) == 0 and (smallSide % 1) == 0:     
        return int (bigSide)
    
print(rectangle(14,10))

def translate(translation, txt):
    """
        myDict = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left', '1':'2'} 
        text = '1 UP, 2 down / left right forward' 
        ">>> translate(myDict, text)
        '2 down 2 up right left forward'
        ">>> text
        '1 UP, 2 down / left right forward'
        ">>> translate({'a':'b'}, text)
        '1 up 2 down left right forward'
    """
  
    # --- YOU CODE STARTS HERE  
    txt = txt.translate(str.maketrans('', '', string.punctuation))
    txt = txt.lower()
    txt = txt.split()
    
    transTxt = ""
    
    for i in txt:
        
        if translation.get(i) == None:
            transTxt = transTxt + i + " "
        if translation.get(i) != None:
            i = translation.get(i)
            transTxt = transTxt + i + " "
    transTxt = transTxt[0:len(transTxt) - 1]
        
    return transTxt
myDict = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left', '1':'2'} 
text = '1 UP, 2 down / left right forward' 
print(translate(myDict, text))

def onlyTwo(x, y, z):
    """
        >>> onlyTwo(1, 2, 3)
        13
        >>> onlyTwo(3, 3, 2)
        18
        >>> onlyTwo(5, 5, 5)
        50
    """
    # --- YOU CODE STARTS HERE
    if x < y and x < z:
        return y*y + z*z
    if y < x and y < z:
        return x*x + z*z
    if z < x and z < y:
        return x*x + y*y
    if x == y and x == z:
        return 2*(x*x)
    
def sumDigits(n):
    """
        >>> sumDigits(1001)
        2
        >>> sumDigits(59872)
        31

    """

    # --- YOU CODE STARTS HERE
    sumDigits = 0
    digits = [int(x) for x in str(n)]
    for i in range(0, len(digits)):
        sumDigits += digits[i]
    return sumDigits


def largeFactor(n):
    """
        >>> largeFactor(15) # factors are 1, 3, 5
        5
        >>> largeFactor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
        40
        >>> largeFactor(13) # factor is 1 since 13 is prime
        1
    """

    # --- YOU CODE STARTS HERE
    largeFactor = 1 
    for i in range (1, n):
        if n % i == 0:
            largeFactor = i
    return largeFactor


def hailstone(n):
    """
        >>> hailstone(10)
        [10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(3.5)
        >>> hailstone(0)
        >>> hailstone(1)
        [1]
        >>> hailstone(27)
        [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(7)
        [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(19)
        [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

    """
    
    # --- YOU CODE STARTS HERE
    if type(n) == int and n > 0:
        
        numbers = [n]
        
        while n != 1:
            if n % 2  == 0:
                n = int (n/2)
                numbers.append(n)
            else:
                n = int ((n*3) + 1)
                numbers.append(n)
            
        return numbers
    
print(hailstone(19))
