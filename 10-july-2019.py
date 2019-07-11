#!/usr/bin/env python
# coding: utf-8

# ### Data Structures
# * Dictionaries
# 

# ### Tuples
# - t1 parenthesis() li square brackets[]
# - differece between list and tuples
#     - list are mutable - can be changed/modified
#          - used to access modify,add,delete data
#     - Tuples are immutable-cannot be changed
#          - used to access data only

# In[12]:


t1 =(1,2,3,4,5,6)
t1
type(t1)


# ### Dictionaries
# * it works on the concept of Set Unique Data
# - Keys,values is the unique identifier for a value
# - Each key is separated from its values with colon(:)
# - Each key and value is separted by comma(,)
# - dictionaries enclosed with curly braces({})

# In[1]:


d1 = { "Name":"Gitam"}
print(d1)


# In[2]:


d1 = {"Name":"Gitam","EmailID":"gitam@gmail.com","Address":"Hyderabad"}
print(d1)


# In[3]:


d1["Name"] #Access the specific value


# In[5]:


d1["EmailID"] = "Gitam-Python@gmail.com" #update the value


# In[6]:


d1["EmailID"]


# In[7]:


del d1["EmailID"] #delete the specific key value


# In[8]:


d1


# In[9]:


d1.keys() # returns thr list if keys


# In[10]:


d1.values() # returns the values


# In[11]:


d1.items() # the list of tuples of keys and valus


# ### Contact Application
# - Add Contact
# - Search the Contact
# - List all contacts
#      - name1:phone1
#      - name2:phone2
# - Modify the Contact
# - Remove the contact
# - Import the contact

# In[18]:


# Add Contact
contacts = {} # Creating a dict object
def addContact(name,phone):
    if name not in contacts:
        contacts[name] = phone
        print("Contact is detai;s are added")
    else:
        print("Contact details are already exits")
    return
addContact("Anil","9876543210")
addContact("Naveen","9966552211")
addContact("Anil","9876543210")


# In[ ]:




