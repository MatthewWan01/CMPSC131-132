# Quiz 1 - Coding Part, Spring 2020
# February, 2020


#QUESTION 1

class Course:
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits
    
    def getCredits(self):
        
        return self.credits
    
class Semester:
    '''
        >>> cmpsc131 = Course("CMPSC 131", 3)
        >>> cmpsc132 = Course("CMPSC 132", 3)
        >>> math230 = Course("MATH 230", 4)
        >>> phys213 = Course("PHYS 213", 2)
        >>> econ102 = Course("ECON 102", 3)
        >>> phil119 = Course("PHIL 119", 3)
        >>> semester = Semester(1)
        >>> semester.addCourse(cmpsc132)
        >>> semester.addCourse(math230)
        >>> semester.isFullTime
        False
        >>> semester.totalCredits
        7
        >>> semester.addCourse(phys213)
        >>> semester.addCourse(econ102)
        >>> semester.addCourse(phil119)
        >>> semester.isFullTime
        True
        >>> semester.dropCourse(phil119)
        >>> semester.addCourse(Course("JAPNS 001", 4))
        >>> semester.totalCredits
        16
        >>> semester.dropCourse(cmpsc131)
        'No such course'
        >>> semester.addCourse(Course(42, "zero credits"))
        'Invalid course'
    '''


    def __init__(self, sem_num):
        # --- YOUR CODE STARTS HERE
        self.sem_num = sem_num
        self.courses = []
          
    def totalCredits(self):
        
        totalCredits = 0
        
        for i in range(len(self.courses)):
            
            totalCredits += self.courses[i].getCredits()
            
        return totalCredits
    
    def isFullTime(self):
        
        if self.totalCredits() >= 12:
            
            return True
        
        return False

    def addCourse(self, course):
        
        if course not in self.courses:
            
            return self.courses.append(course)
        
        else:
            
            return 'Invalid course'
        
    def dropCourse(self, course):
        
        if course in self.courses:
            
            return self.courses.remove(course)
            
        return 'No such course'
    
# QUESTION 2

class Vector:
    '''
        >>> Vector([1,2])+Vector([5])
        'Error - Invalid dimensions'
        >>> Vector([1,2])+Vector([5,2])      # 1+5, 2+2
        <6, 4>
        >>> x=Vector([2,4,6])
        >>> y=Vector([2,4,6])
        >>> c=x+y
        >>> isinstance(c, Vector)
        True
        >>> print(c)
        <4, 8, 12>
        >>> x*5       # 5*2, 5*4, 5*6
        <10, 20, 30>
        >>> 5*x
        <10, 20, 30>
    '''
   
    def __init__(self, vector):
        self.vector = vector
    
    def __str__(self):
        return "<{}>".format(str(self.vector)[1:-1])

    # --- YOUR CODE STARTS HERE
    def __add__(self, other):
        
        if len(self) != len(other):
            return 'Error - Invalid dimensions'
        else:
            for i in len(self):
                return self[i] + other[i]
                
    def __mult__(self, other):
        for i in len(self):
            return self[i] * other
        
    def __rmult__(other, self):
        for i in len(self):
            return self[i] * other
        
    def __len__(self):
        num = 0 
        for i in self:
            num += 1
        return num\
