#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python 3 Program to print Fibonacci 
# series in reverse order 
  
def reverseFibonacci(n): 
   
    a = [0] * n  
  
    # assigning first and second elements 
    a[0] = 0 
    a[1] = 1 
  
    for i in range(2, n):   
  
        # storing sum in the 
        # preceding location 
        a[i] = a[i - 2] + a[i - 1]  
       
  
    for i in range(n - 1, -1 , -1):   
  
        # printing array in 
        # reverse order 
        print(a[i],end=" ")  
       
   
  
# Driver function 
n = 5 
reverseFibonacci(n) 


# In[2]:


def reverseFibonacci(n): 

 a = [0] * n  
  
 # assigning first and second elements 
 a[0] = 0 
 a[1] = 1 
  
 for i in range(2, n):   
  
     # storing sum in the 
     # preceding location 
     a[i] = a[i - 2] + a[i - 1]  
    
  
 for i in range(n - 1, -1 , -1):   
  
     # printing array in 
     # reverse order 
     print(a[i],end=" ")  
    

  
# Driver function 
n = 12 
reverseFibonacci(n)


# In[1]:


#*** Function to count the occurances of a character in a string
def repeat(x,target):
 c=0
 for i in x:
     if i==target:
         c+=1
 return c
# (OR)
#def repeat1(x,target):
#    return x.count(target)
n=str(input("enter a string-"))
m=str(input("enter target element-"))
repeat(n,m)


# In[ ]:


def Q1(x):
    while x-2!=0:
        a=0
        b=1
        c=0
        for i in range(x-2):
            c=a+b
            a=b
            b=c
        print(c,end=" ")
        x-=1
    print('1 0')
    return
Q1(int(input("enter number")))


# In[ ]:


def Q2(n):
    a=[]
    s=0
    for i in range(n):
        a.append(int(input()))
    for i in range(n):
        c=0
        for j in range(n):
            if i!=j:
                if a[i]==a[j]:
                    c+=1
    if c==0:
        s=s+a[i]
    return s
Q2(int(input("no of values")))


# In[ ]:


def Q3(a,b):
    if len(a)<=len(b):
        n=len(a)
        k=len(b)
    else:
        n=len(b)
        k=len(a)
    for i in range(n):
        print(a[i],b[i])
    for j in range(n,k):
        if(len(a)<=len(b)):
            print(b[j],'*')
        else:
            print(a[j],'*')
    return
x=str(input("enter str:"))
x=x.split()
Q3(x[0],x[1])


# In[ ]:


def Q4(a,b):
    if len(a)>=len(b):
        print(a.upper())
    else:
        print(b.upper())
    return
x=str(input("enter str:"))
x=x.split()
Q4(x[0],x[1])


# In[ ]:




