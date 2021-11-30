#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 23:31:48 2019

@author: mzwonton
"""

###Kyle Robertson, Andrew Rednikov, Adarsh Subramanian, Matthew Wan

finalbooklist = open("finalbooklist.txt","r")
finallibrarylog = open("finallibrarylog.txt","r")

bookName = []
imp = []
copyNumber = []
dayAdded = []
borrower = []
dayBorrowed = []
dayToReturn = []
daysUsed = []
books = []
fineNames = []
fineAmount = []
totalUse = []
daysAvailible = []
totalDays = []


lineA = "placeholder"   #lineA=current line in booklist
while lineA != "":
    lineA = finalbooklist.readline()
    if lineA != "":
        a = lineA.split("#")
        a[-1] = a[-1].strip()
        
        numCopies = int(a[1])
        
        for i in range(numCopies):     
            bookName.append(a[0])      #creates bookName list from booklist
            imp.append(a[2])           #creates imp (important) list from booklist
            copyNumber.append(i+1)     #creates copyNumber list from booklist
            borrower.append("")        #creates creates empty set with corresponding book
            dayBorrowed.append("")
            dayToReturn.append(-1)
            dayAdded.append(1)
            daysUsed.append(0)
            daysAvailible.append(0)
        books.append(a[0])     
            
       
        
lineB = "placeholder"     #lineB=current line in librarylog
while lineB != "":
    lineB = finallibrarylog.readline()
    if lineB != "":
        b = lineB.split("#")
        b[-1] = b[-1].strip()
        #print(b)


        if len(b) == 1:         #current day number at end
            currentDay = b[0]
                        
            
        
        if len(b) == 3:       #if a book is added
            bookName.append(b[1])
            imp.append(b[2])
            copyNumber.append(1)    #only works if book is new(comeback)
            borrower.append("")
            dayBorrowed.append("")
            dayToReturn.append(-1)
            dayAdded.append(b[0])
            daysUsed.append(0)
            books.append(b[1])
            daysAvailible.append(0)



        if len(b) == 4 and b[3] != 'RET' and b[0] != 'PAY':   #checkout      
            i=0
            while i != -1:
                if b[1] == bookName[i] and borrower[i] == "":
                    borrower[i]=b[2]        #add person, day borrowed, day to be returned
                    dayBorrowed[i]=b[0]
                    dayToReturn[i]= int(b[3])+int(b[0])
                    i = -1
                else:
                    i = i+1

                    

        if len(b) == 4 and b[3] == 'RET':    #return

            i=0
            while i != -1:                    #calculates days used
                if b[1] == bookName[i] and b[2]==borrower[i]:
                    daysUsed[i] = daysUsed[i]+(int(b[0])-int(dayBorrowed[i]))
                    i = -1
                else:
                    i = i+1


            i=0
            while i != -1:
                if b[1] == bookName[i] and b[2]==borrower[i]:
                    if int(b[0])>dayToReturn[i]:        #a fine is needed
                        fineNames.append(b[2])
                        fine = 0
                        if imp[i] == "True":
                            fine = 15*(int(b[0])-dayToReturn[i])
                        else:
                            fine = 5*(int(b[0])-dayToReturn[i])
                        fineAmount.append(fine)
                            
                        j = 0
                        while j < len(fineNames)-1:          #checks if person already has fine
                            if fineNames[len(fineNames)-1]== fineNames[j]:
                                fineNames.pop()

                                k=0
                                while k < len(fineAmount):
                                    if b[2] == fineNames[k]:
                                        fineAmount[k]= fineAmount[k]+fineAmount[len(fineAmount)-1]
                                        fineAmount.pop()
                                        break
                                    else:
                                        k=k+1   
                            else:
                                j = j+1
                                
                    borrower[i]= ""       #remove person, day borrowed, day to be returned
                    dayBorrowed[i]= ""
                    dayToReturn[i]= -1
                    i = -1
                else:
                    i = i+1

        
        if len(b) == 4 and b[0] == 'PAY':  #PAY
            for i in range(len(fineNames)):
                if b[2] == fineNames[i]:
                    fineAmount[i] = fineAmount[i]-int(b[3])

finalbooklist.close()
finallibrarylog.close()

for i in range(len(borrower)):   #adds usage to pending returns
    if borrower[i] != "":
        daysUsed[i]=daysUsed[i]+(int(currentDay)-int(dayBorrowed[i]))


for i in range(len(borrower)):             #gives fine if pending books are overdue
    if borrower[i] != "" and 0<dayToReturn[i]<int(currentDay):
        fineNames.append(borrower[i])
        j = 0
    if dayToReturn[i] != "" and 0<dayToReturn[i]<int(currentDay):
        fine = 0
        if imp[i] == "True":
            fine = 15*(int(currentDay)-dayToReturn[i])
        else:
            fine = 5*(int(currentDay)-dayToReturn[i])
        fineAmount.append(fine)

        while j < len(fineNames)-1:          #checks if person already has fine
            if fineNames[len(fineNames)-1]== fineNames[j]:
                fineNames.pop()
                
                k=0
                while k < len(fineAmount):
                    if borrower[i] == fineNames[k]:
                        fineAmount[k]= fineAmount[k]+fineAmount[len(fineAmount)-1]
                        fineAmount.pop()
                        break
                    else:
                        k=k+1
                                    
            else:
                j = j+1



for i in range(len(dayAdded)):         #creates day availible list
    daysAvailible[i]= int(currentDay)-int(dayAdded[i])

for i in range(len(copyNumber)):   #adds days used per book
    j = 0
    if copyNumber[i] ==1:
        totalUse.append(daysUsed[i])
        j = j+1
    else:
        j = j-1
        totalUse[j] = totalUse[j]+daysUsed[i]
    
for i in range(len(copyNumber)):
    j = 0
    if copyNumber[i]==1:
        totalDays.append(daysAvailible[i])
        j = j+1
    else:
        j=j-1
        totalDays[j] = totalDays[j]+daysAvailible[i]
        



print()
print("Current Day: ",currentDay)
print()
print("Book Names: ",bookName)
print()
print("Importance: ",imp)
print()
print("Copy number: ",copyNumber)
print()
print("Day added: ",dayAdded)
print()
print("Borrower: ",borrower)
print()
print("Day borrowed: ",dayBorrowed)
print()
print("Day to be returned: ",dayToReturn)
print()
print("Days used: ", daysUsed)
print()
print("Fine Names :",fineNames)
print()
print("Fine Amounts: ",fineAmount)
print("Books : ",books)
print()
print("Total Use: ",totalUse)
print()
print("Days availble :",daysAvailible)
print()
print("Total Days :",totalDays)
                        


def checkout(student, book):
    result1="no"
    for i in range(len(bookName)):
        if book == bookName[i] and borrower[i]=="":
            result1="yes"
            break
        
    result2 = "yes"           
    for i in range(len(fineNames)):
        if student == fineNames[i] and fineAmount[i]>50:
            result2 = "no"
            break
        
    if result1 == "yes" and result2 == "yes":
        print("Yes")
    else:
        print("No")


def returnBook(student, book):
    result1="no"
    for i in range(len(bookName)):
        if book == bookName[i] and borrower[i]==student:
            result1="yes"
            break
        
    if result1 == "yes":
        print("Yes")
    else:
        print("No")


def feesList():
    print()
    print("---------FEES LIST------")
    for i in range(len(fineAmount)):      #selection sort for fineAmount
        min = i
        for j in range(i+1,len(fineAmount)):
            if fineAmount[min] > fineAmount[j]:
                min = j
        fineAmount[i], fineAmount[min] = fineAmount[min], fineAmount[i]
        fineNames[i], fineNames[min] = fineNames[min], fineNames[i]     #corresponding fineName gets sorted accordingly
    fineAmount.reverse()
    fineNames.reverse()

    
    fines = [[0]*2 for i in range(len(fineNames))]          #makes fine Names and fine Amount into 2d list
    k = 0
    for i, j in zip(fineNames,fineAmount):
        fines[k][0]=i
        fines[k][1]=j
        k+=1
    print("Fines :",fines)

def usage():
    print()
    print("---------USEAGE-----")
    usage = []
    for i in range(len(totalUse)):     #calculates usage per book
        usage.append((totalUse[i]/totalDays[i])*100)

        
    for i in range(len(usage)):      #selection sort for usage
        min = i
        for j in range(i+1,len(usage)):
            if usage[min] > usage[j]:
                min = j
        usage[i], usage[min] = usage[min], usage[i]
        books[i], books[min] = books[min], books[i]     #corresponding fineName gets sorted accordingly
    usage.reverse()
    books.reverse()

    
    use = [[0]*2 for i in range(len(books))]          #makes fine Names and fine Amount into 2d list
    k = 0
    for i, j in zip(books,usage):
        use[k][0]=i
        use[k][1]=j
        k+=1
    print(use)
    
        
    

    
checkout("Arjun G","Eye of the world, Jordan")
checkout("Piotr B","Eye of the world, Jordan")
checkout("Sunny P","The gathering storm, Jordan")
checkout("Arjun G","String Theory, Suskind")
checkout("Ishan B","Loop Quantum Gravity, Gambini")
feesList()
usage()

print("Done")
