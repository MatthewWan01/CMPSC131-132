#HW3
#Due Date: 03/27/2020, 11:59PM 
########################################
#                                      
# Name: Matthew Wan
# Collaboration Statement: discussed with Michael Grossman and Kelp Patel on creating 
#expressions for getPostFix and used online resources to see how people seperated digits and operators for the txt         
#
########################################
import re

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

#=============================================== Part I ==============================================

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        # YOU ARE NOT ALLOWED TO MODIFY THE CONSTRUCTOR
        self.top = None
        self.count=0
    
    def __str__(self):
        # YOU ARE NOT ALLOWED TO MODIFY THE THIS METHOD
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__

    def isEmpty(self): 
        # YOUR CODE STARTS HERE
        if self.count == 0: #Empty
            return True
        return False

    def __len__(self): 
        # YOUR CODE STARTS HERE
        return self.count #return length

    def push(self,value):
        # YOUR CODE STARTS HERE
        node = Node(value) #Make new node
        
        if self.top is None: #stack is empty
            self.top = node
            self.count += 1
            return None
        
        else: #Stack not empty
            
            node.next = self.top 
            self.top = node
            self.count += 1
            return None
            
    def pop(self):
        # YOUR CODE STARTS HERE
        if self.top is None: #stack is empty
            return None
        
        temp = self.top #store prev top
        self.top = self.top.next #value unter top
        self.count -= 1
        return temp.value
        

    def peek(self):
        # YOUR CODE STARTS HERE
        if self.isEmpty:
            return None
        return self.top.value #return top of stack
    

#=============================================== Part II ==============================================
class Calculator:
    def __init__(self):
        self.__expr = None

    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str) and len(new_expr.strip())>0:
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None


    def isNumber(self, txt):
        if not isinstance(txt,str) or len(txt.strip())==0:
            print("Argument error in isNumber")
            return False
        # YOUR CODE STARTS HERE
        try: #try execption
            float(txt) or int(txt) #if can be written as float or int
            return True
        except ValueError: # if not
            return False




    def _getPostfix(self, txt):
        '''
            Required: _getPostfix must create and use a Stack for expression processing. Follow PEMDAS
            >>> x=Calculator()
            >>> x._getPostfix(' 2 ^        4')
            '2.0 4.0 ^'
            >>> x._getPostfix('2')
            '2.0'
            >>> x._getPostfix('2.1*5+3^2+1+4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('    2 *       5.34        +       3      ^ 2    + 1+4   ')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix(' 2.1 *      5   +   3    ^ 2+ 1  +     4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('(2.5)')
            '2.5'
            >>> x._getPostfix ('((2))')
            '2.0'
            >>> x._getPostfix ('     2 *  ((  5   +   3)    ^ 2+(1  +4))    ')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('  (   2 *  ((  5   +   3)    ^ 2+(1  +4)))    ')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('  ((   2 *  ((  5   +   3)    ^ 2+(1  +4))))    ')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('   2 *  (  5   +   3)    ^ 2+(1  +4)    ')
            '2.0 5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            # If you are veryfing the expression in calculate before passing to postfix, this cases are not necessary

            >>> x._getPostfix('2 *    5   +   3    ^ -2       +1  +4')
            >>> x._getPostfix('2    5')
            >>> x._getPostfix('25 +')
            >>> x._getPostfix('   2 *  (  5   +   3)    ^ 2+(1  +4    ')
            >>> x._getPostfix('2*(5 +3)^ 2+)1  +4(    ')
        '''
        if not isinstance(txt,str) or len(txt.strip())==0:
            print("Argument error in _getPostfix")
            return None

        postfix_Stack=Stack()
        # YOUR CODE STARTS HERE
        postfix = "" #empty string
        digits = "0123456789." #numbers
        operators = "()^*/+-" #operators
        expression = [] #empty list
        isNumber = False 
        isSpace = False
        temp = ""
        prec = {'^':5, '*':4, '/':4, '+':3, '-':3, '(':2, ')':1} #PEMDAS

        for i in txt: #going through txt
            
            if i in digits and isSpace == False: #if is a number
                isNumber = True
                isSpace = False
                continue
            
            elif i == " ": #empty space
                isSpace = True
                continue
            
            elif i in operators: #is an operator
                isNumber = False
                isSpace = False
                continue
            
            if isNumber == True and isSpace == True: 
                if i in digits: #if found a digit and another digit is found after space
                    return None
            
        for i in txt: #go through txt
            if i == " ": #space
                continue
            
            elif i in operators: #operator
                if temp != "": #is operator
                    expression.append(temp)
                    expression.append(i)
                    temp = ""
                    
                else: #empty
                    expression.append(i)
                    continue
                
            elif i in digits: #is number
                temp += i
            
        if temp != "": #is not operators ie ()
            expression.append(temp)
        
        for i in expression: #go through expression list
            
            if len(expression) % 2 != 0: #cannot have even elements 
                
                if (self.isNumber(i)): #is a number
                    postfix = postfix + str(float(i)) + " "
                    
                elif i in "+-*/^": #operator
                    while postfix_Stack.top != None and prec.get(i) <= prec.get(postfix_Stack.top.value): #change order of PEMDAS
                        postfix = postfix + postfix_Stack.pop() + " "
                    postfix_Stack.push(i)
                    
                elif i == '(': #parenthesis
                    postfix_Stack.push(i)
                
                elif i == ')':
                    k = postfix_Stack.pop()
                    while k != '(':
                        if postfix_Stack.top == None:
                            return None
                        postfix = postfix + k + " "
                        k = postfix_Stack.pop()

        while postfix_Stack.top != None:
            postfix = postfix + postfix_Stack.pop() + " "

        postfix = postfix[0: len(postfix)-1] #get rid of space at end
        
        return postfix
   

    @property
    def calculate(self):
        '''
            Required: calculate must call postfix
                      calculate must create and use a Stack to compute the final result as shown in the video lecture
            >>> x=Calculator()
            >>> x.setExpr('    4  +      3 -2')
            >>> x.calculate
            5.0
            >>> x.setExpr('  2  +3.5')
            >>> x.calculate
            5.5
            >>> x.setExpr('4+3.65-2 /2')
            >>> x.calculate
            6.65
            >>> x.setExpr(' 23 / 12 - 223 +      5.25 * 4    *      3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr('   2   - 3         *4')
            >>> x.calculate
            -10.0
            >>> x.setExpr(' 3 *   (        ( (10 - 2*3)))')
            >>> x.calculate
            12.0
            >>> x.setExpr(' 8 / 4  * (3 - 2.45      * (  4- 2 ^   3)) + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr(' 2   *  ( 4 + 2 *   (5-3^2)+1)+4')
            >>> x.calculate
            -2.0
            >>> x.setExpr('2.5 + 3 * ( 2 +(3.0) *(5^2 - 2*3^(2) ) *(4) ) * ( 2 /8 + 2*( 3 - 1/ 3) ) - 2/ 3^2')
            >>> x.calculate
            1442.7777777777778
            

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            >>> x.setExpr("4++ 3 +2") 
            >>> x.calculate
            >>> x.setExpr("4    3 +2")
            >>> x.calculate
            >>> x.setExpr('(2)*10 - 3*(2 - 3*2)) ')
            >>> x.calculate
            >>> x.setExpr('(2)*10 - 3*/(2 - 3*2) ')
            >>> x.calculate
            >>> x.setExpr(')2(*10 - 3*(2 - 3*2) ')
            >>> x.calculate
        '''

        if not isinstance(self.__expr,str) or len(self.__expr.strip())==0:
            print("Argument error in calculate")
            return None

        calculator_Stack=Stack()
        # YOUR CODE STARTS HERE
        postExpression = self._getPostfix(self.__expr) #create new expression
        if postExpression != None: #is an expression
            operators = "^*/+-"
            
            postExpression = postExpression.split() #make list
            for i in postExpression: #go through list
                if self.isNumber(i) == True: #is number
                    calculator_Stack.push(i)
                elif i in operators: #is operator
                    n1 = float(calculator_Stack.pop()) #change string into float
                    n2 = float(calculator_Stack.pop()) 
                    
                    #Operators
                    if i == '+': 
                        result = n2 + n1
                    if i == '-':
                        result = n2 - n1
                    if i == '*':
                        result = n2 * n1
                    if i == '/':
                        result = n2 / n1
                    if i == '^':
                        result = pow(n2, n1)
                        
                    calculator_Stack.push(result) #answer
                    
            final = calculator_Stack.pop() #get answer
            if len(calculator_Stack) != 0: #another item in stack
                return None
            
            return final
        
        else: #if no expression
            return None
