#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt 
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


# In[3]:


supermarket = pd.read_csv("Stores.csv")


# In[4]:


supermarket


# In[5]:


supermarket.head()


# In[6]:


supermarket.shape


# In[7]:


supermarket.info() # No null entries 


# In[8]:


supermarket.describe()


# In[9]:


plt.hist(supermarket["Store_Area"], bins = 50)
plt.xlabel("Area of Supermarket Store")
plt.ylabel("Number of Supermarket Stores")
plt.show()


# In[10]:


plt.hist(supermarket["Items_Available"], bins = 20)
plt.xlabel("Number of Items Available")
plt.ylabel("Number of Supermarket Stores")
plt.show()


# In[11]:


plt.hist(supermarket["Daily_Customer_Count"], bins = 40)
plt.xlabel("Daily Customer Count")
plt.ylabel("Number of Supermarket Stores")
plt.show()


# In[12]:


plt.hist(supermarket["Store_Sales"], bins = 30)
plt.xlabel("Store Sales")
plt.ylabel("Number of Supermarket Stores")
plt.show()


# In[13]:


plt.scatter(supermarket["Store_Area"], supermarket["Store_Sales"])
plt.xlabel("Area of Supermarket Store")
plt.ylabel("Store Sales")
plt.show()


# In[14]:


plt.scatter(supermarket["Items_Available"], supermarket["Store_Sales"])
plt.xlabel("Number of Items Available")
plt.ylabel("Store Sales")
plt.show()


# In[15]:


plt.scatter(supermarket["Daily_Customer_Count"], supermarket["Store_Sales"])
plt.xlabel("Daily Customer Count")
plt.ylabel("Store Sales")
plt.show()


# In[16]:


corr = supermarket.corr()
print(corr["Store_Sales"])

