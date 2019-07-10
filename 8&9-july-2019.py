#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Function to find the prime numbers count from 1 to N
# 10 -- 4(2,3,5,7)
def primeCount(n):
    cnt = 0
    for a in range(2,n+1):
        k = 0
    for i in range(2,a//2+1):
            if a % i == 0:
                k = k + 1
            if (k<=0):
                cnt = cnt + 1
            return cnt
    primeCount(10)


# In[19]:


# Individual digit factorial sum is sa,e as original number
# Example :-
# 145 -- Yes (5!+ 4! + 1! = 145)
# 123 -- No (3! + 2! + 1! = 9)
def factorial(n):
   fact = 1
   for i in range(2,n+1):
       fact *= i
   return fact
def digitfactSum(n):
   sum = 0
   buffer = n
   while n != 0:
       r = n%10
       sum += factorial(r)
       n = n // 10
   if sum == buffer:
       return "Yes"
   else:
       return "No"
   return
print(digitfactSum(145))
print(digitfactSum(123))


# In[1]:


# Function to return the count of palindrome number two limits
# Input : 1 10
# Output : 9(1,2,3,4,5,6,7,8,9)


# Onput : 11 100
# Output: 9(11,22,33,44......,99)
def ispalindrome(n):
   rev = 0
   buffer = n
   while n!= 0:
       r = n % 10
       rev = rev * 10 + r
       n = n // 10
   if rev == buffer:
       return True
   else:
       return False
   return
def countpalindrome(lb,ub):
   cnt = 0
   while lb !=ub:
       # Implement
       if ispalindrome(lb) == True:
           cnt = cnt + 1
       lb = lb + 1
   return cnt
countpalindrome(1,10)


# In[1]:


# Extract digits from given string
def extractdigits(str):
    for x in range(len(str)):
        if ord(str[x])>=48 and ord(str[x])<=57:
            print(str[x],end=" ")
    return 
extractdigits("appli1cat8ion89")  


# In[2]:


#function to return the sum of the digits
def sumofdigits(str):
    sum=0
    for x in range(len(str)):
        if ord(str[x])>=48 and ord(str[x])<=57:
            sum=sum+(ord(str[x])-48)
    return sum
sumofdigits("appli1cat8ion89")


# In[3]:


def sumofdigits(str):
    sum=0
    for x in range(len(str)):
        if ord(str[x])>=48 and ord(str[x])<=57:
            if (ord(str[x])-48)%2==0:
                sum=sum+(ord(str[x])-48)
                
    return sum
sumofdigits("appli1cat8ion89")


# # Function of the list
# lst1
# print(min(lst1))
# print(max(lst1)) Day objectives
# Python data structures
# Lists
# Tuples
# Dictionaries
# Basic Program sets on data structures
# advanced problem set
# contact application(dictionary object)
# Data structures
# To store ,search and Sort the data
# pyhton data structures
# lists
# It is one of the common data structures supports by python,the list items are separated by comma operator and enclosed in square brackets
# example:
# list1 = [1,6,2,18,9]
# list2 = ["gitam",12,12,15.5,"hyderabad"]
# print(sum(lst1))
# print(sum(lst1)//len(lst1))
# print(sum(lst1[1::2])/len(lst1[1::2]))

# In[4]:


lst = [1,8,16,9,2]
print(lst)
print(lst[0])
print(lst[1])
print(lst[-1])
print(lst[-2])
print(lst[2])
print(lst[1:])


# In[5]:


# Update the list item values using index(Direct referencing)
li = ["Gitam","Python",1989,2002]
print(li)
li[2] = 2019
print(li)


# In[6]:


# basic list opertaions
lst1 = [1,9,6,18,2]
print(len(lst1))
print(lst1*2)
print(len(lst1))
print(9 in lst1)
print(15 in lst1)
for x in range(len(lst1)):
    print(lst1[x],end=' ')


# In[7]:


# Function of the list
lst1
print(min(lst1))
print(max(lst1))
print(sum(lst1))
print(sum(lst1)//len(lst1))
print(sum(lst1[1::2])/len(lst1[1::2]))


# In[1]:


li = [1,9,8,2,6,3]
print(li[-1::-2])
li = [1,9,8,2,6,3]
print(li[-1:2:-2])
li = [1,9,8,2,6,3]
print(li[-1:0:-2])
li = [1,9,8,2,6,3]
print(li[-1:2:-2])


# In[2]:


# Function to find the second large item from the list
# input :   [1,19,6,2,8,18,3]
# output :  18
def secondlarge(li):
   li.sort()
   return li[-2]
def genericlarge(li,n):
   li.sort()
   return li[-n]
li= [1,19,6,2,8,18,3]
genericlarge(li,4)


# # Linear search
# Linear search algorithm can be applied on duplicate and unique list
# Unique list : All items of the list are appeared as only one
# Duplicate list : The items of the list can be appeared more than one
# Linear search algorithm can be applied on sorted list or unsorted list

# In[3]:


# Function to search the data in a list
# Search is found then return the index if not return -1
def linearsearch1(li,taritem):
   for x in range(len(li)):
       if li[x] == taritem:
           return x
       return -1
li = [1,19,6,2,8,18,3]
linearsearch1(li,225)


# In[4]:


# Function
# Input : [1,5,9,6,5,15,1,2,5],key=5 # Duplicate
# Output : 1 4 8
def linearsearch2(li,taritem):
   for x in range(len(li)):
       if li[x] == taritem:
           print(x,end=" ")
   return 

li = [1,5,9,6,5,15,1,2,5]
linearsearch2(li,5)


# In[5]:


# Function
# i/p : list
#o/p : seq of characters
# Test case
# [1,5,9,6,5,15,1,2,5],tar=5 --!! !!!!! !!!!!!!!!

def linearSearch3(li,tarItem):
   # Implement the logic
   for x in range(len(li)):
       if li[x] == tarItem:
           j=0
           while j!=x+1:
               print("!",end=" ")
               j=j+1
           print(end=" ")
   return
li = [1,5,9,6,5,15,1,2,5]
linearSearch3(li,5)


# In[6]:


# Function
# i/p: List
# o/p: Formatted
# Test case:
# [12,2,45,9,18,15,36] --60
#A list item which is perfectly multiple of 3 and 5

def linearSearch4(li):
   sum=0
   for x in range(len(li)):
       if li[x] %3 ==0 and li[x] % 5==0 :
           sum += li[x] #sum=sum + li[x]
   return sum
li= [12,2,45,9,18,15,36]
linearSearch4(li)


# In[ ]:




