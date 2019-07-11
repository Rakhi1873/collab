#!/usr/bin/env python
# coding: utf-8

# In[54]:


# 1st answer
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


# In[3]:


# 2nd answer
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


# In[57]:


# 3rd answer
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


# In[4]:


# 4th answer
def Q4(a,b):
    if len(a)>=len(b):
        print(a.upper())
    else:
        print(b.upper())
    return
x=str(input("enter str:"))
x=x.split()
Q4(x[0],x[1])


# In[1]:


# 5th ANSWER
def Q5_1(a):
    a=a.split()
    for i in range (len(a)):
        if a[i].istitle()==True:
            print(a[i].upper(),end= " ")
    return
x=str(input("enter str:"))
Q5_1(x)


# In[64]:


# 7th answer
def Q7(n):
    for i in range(len(n)):
        n[i]=int(n[i])
    for i in range(len(n)):
        for j in range(n[i]):
            print("*",end="")
        print("")
    return
x=input("enter num")
Q7(list(x))


# In[5]:


def fact(a):
    f=1
    for i in range (1,a+1):
        f*=i
    return f   
def series(m):
    s=0
    for x in range (1,n+1):
        s=s+fact(x)
    return s
n=int(input("enter n"))
series(n)


# In[6]:


def series(n):
    a=1
    b=3
    c=a+b
    print(a,b,c,end=" ")
    for i in range (4,n+1):
        d=a+b+c
        a=b
        b=c
        c=d
        print(d,end=" ")
    return
n=int(input("enter a number"))
series(n)


# In[7]:


def square(n):
    for i in range(n):
        print(2**i,end=" ")
    return
n=int(input("enter a number"))
square(n)


# In[8]:


def square(n):
    for i in range(n):
        print(3**i,end=" ")
    return
n=int(input("enter a number"))
square(n)


# In[9]:


def comb(a,b):
    c=a+b
    return c 
a=str(input("enter a string "))
b=str(input("enter a string "))
comb(a,b)


# In[10]:


#HebeonTech,e -- HbonTch
def delete(n,target):
    c=0
    for i in range(len(n)):
        if n[i]==target:
            c+=1
    print(n.replace(target,"",c))
n=str(input("enter a string"))
target=str(input("enter a char"))
delete(n,target)


# In[ ]:




