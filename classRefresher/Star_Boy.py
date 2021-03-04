#!/usr/bin/env python
# coding: utf-8

# In[ ]:


df.sort_values(['Years Experience'])


# In[25]:


degree_counts.plot(kind = 'pie' )


# In[3]:


import pandas as pd
df = pd.read_csv("PastHires.csv")
df.head()


# In[4]:


df.tail(4)


# In[5]:


df.shape


# In[6]:


df.size


# In[7]:


df.columns


# In[8]:


len(df)


# In[11]:



df.index


# In[14]:


df["Hired"]


# In[15]:


df["Hired"][:5]


# In[16]:


df["Hired"][5]


# In[19]:


df[['Years Experience','Hired']]


# In[22]:


degree_counts = df['Level of Education'].value_counts()
degree_counts

degree_counts.plot(kind = 'pie' )
# In[27]:


degree_counts.plot(kind = 'bar' )


# In[28]:


df[['Previous employers', 'Hired']] [5:10]


# In[33]:


df2 = df[['Previous employers', 'Hired']] [5:10]


# In[32]:


df2.plot(kind = 'bar')


# In[34]:


df2 = df[['Previous employers', 'Hired']] [5:11]


# In[35]:


df2 = df[['Previous employers', 'Hired']] [5:10]
df2


# In[36]:


df2.plot(kind='bar')


# In[ ]:




