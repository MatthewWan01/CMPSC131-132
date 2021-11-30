#Lab #1
#Due Date: 01/24/2020, 11:59PM 
########################################
#                                      
# Name: Matthew Wan
# Collaboration Statement: Discussed Michael Grosman on how to remove non-alphabet-character strings in list as well as using online resourses to help solve such issues   
# Links: https://stackoverflow.com/questions/3159155/how-to-remove-all-integer-values-from-a-list-in-python
########################################

# NOTE: If you use input() for testing, don't forget to remove it before submitting
import string
import re

def common(list1, list2):
    #"""
        #>>> common([12,3,5,8,90,11,44,66,8,9,34,56,-1,0,5,3333,3,2,1],[12,3,3,3,3,3,3,3,3,3,3,3,3,3,1,1,44])
        #[44, 12, 3, 1]
        #>>> common([1,2,3],[4,5,6])
        #[]
    #"""
    # --- YOU CODE STARTS HERE
    common = []
    for i in range (0, len(list1)):
        for j in range (0, len(list2)):
            if list1[i] not in common:
                if list1[i] == list2[j]:
                    common.append(list1[i])
    common.sort(reverse = True)    
    return common

def connect(list1, list2, k):
    #"""
        #>>> connect([1,2,3,4], [5,6], 2)
        #[1, 2, 5, 6, 3, 4]
        #>>> connect([1,2,3,4], [5,6,7,8,9,10], 3)
        #[1, 2, 3, 5, 6, 7, 8, 9, 10, 4]
    #"""
    # --- YOU CODE STARTS HERE
    connect = []
    for i in range (0, k):
        connect.append(list1[i])
    for i in range (0, len(list2)):
        connect.append(list2[i])
    for i in range(k, len(list1)):
        connect.append(list1[i])   
    return connect

def countWords(document):
    #"""
        #>>> expected={'he': 4, 'will': 2, 'be': 1, 'the': 3, 'president': 2, 'of': 3, 'company': 1, 'right': 1, 'now': 1, 'is': 2, 'a': 1, 'vice': 1, 'but': 1, 'himself': 1, 'no': 1, 'sure': 1, 'it': 1, 'later': 1, 'see': 1, 'importance': 1, 'these': 1}
        #>>> countWords('article.txt')==expected
        #True
    #"""

    # Open the file and read the contents
    f = open(document,"r")

    if f.mode == 'r': # Verify that the file was opened
        contents = f.read() # use the read() function to read the entire file, contents has the data as string
        contents = contents.translate(str.maketrans('', '', string.punctuation))
        contents = contents.replace('\n', ' ')
        contents = contents.lower()
        contents = contents.split()
        contents = [x for x in contents if not (x.isdigit() or x[0] == '-' and x[1:].isdigit())]
        #alter list to make each element a word
        
        
        dic = {}
        for i in contents:
            if dic.get(i) == None:
                dic[i] = 1
            elif dic.get(i) != None:
                if dic.get(i) > 0:
                    dic.update({i: dic.get(i) + 1})
        #Count the occurance of each word        
    return dic          
        
    # --- YOU CODE STARTS HERE  