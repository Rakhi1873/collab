#!/usr/bin/env python
# coding: utf-8

#    REGULAR EXPRESSION
# pattren matching
# pattren(re) package
# [0-9]--> any digit matching
# --> two digit number(^[0-9]{2}$) --> five digit number[(0-9)5]

# ### REGULAR EXPRESSION FOR CHARACTERS
# - [a-z]-->any lower case characters
# - [A-Z]-->any upper case characters
# - ^[a-z]{5}$ --> it accept 5 lower characters
# ​
# - ^[a-zA-Z]{8}$-->accepts 8 characters can be anything lower and upper
# ​
# - ^[a-zA-Z0-9]{8}$--> Accept 8characters can be anything lower upper and digit

# In[5]:


# function to test two digit number matching
import re
def twodigitmatching(n):
   pattren = '^[0-9]{2}$'
   n=str(n)
   if re.match(pattren,n):
       return True
   return False
print(twodigitmatching(12)) # True
print(twodigitmatching(123)) # False


# In[16]:


pattern='^(a-zA-Z){8}$'
      if re.match(pattern,s):
      return True
      return False
print(testUsername('GitamHYD'))
print(testUsername('Gitam188'))


# In[ ]:


# function to define to test username having 8 characters
# upper case and lower
def testusername(s):
   pattern='^(a-zA-Z){8}$'
   if re.match(pattern,s):
       return True
   return False
print(testusername('GitamHYD'))
print(testusername('Gitam188'))


#     -- Regular expression to validate the rollnumber
#    
#   Example : 1521A0501
#   Example : 1521A0109
#   Example : 1521A0499
#   
#     -- Regular expression to validate the passward
# 
#   parameters : len min of 6 characters and max of 15 characters
#   Accept Lower case, upper case, digits, splchar(@ ,#,$,!)

# In[17]:


# function to validate the indian mobile number
def phonenumbervalidation(phone):
    pattern = '^[+][9][1][6-9][0-9]{9}$|^[0][6-9][0-9]{9}$|^[6-9][0-9]{9}$'
    phone = str(phone)
    if re.match(pattern,phone):
        return True
    return False
phonenumbervalidation('9988774455')


# In[18]:


# function to define to test username having 8 characters
# upper case and lower
def testusername(s):
    pattern='^(a-zA-Z){8}$'
    if re.match(pattern,s):
        return True
    return False
print(testusername('GitamHYD'))
print(testusername('Gitam188'))


# In[ ]:




