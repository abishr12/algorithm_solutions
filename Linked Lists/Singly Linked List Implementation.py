
# coding: utf-8

# In[7]:


class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None


# In[8]:


a = Node(1)
b = Node(2)
c = Node(3)


# In[9]:


a.nextnode = b


# In[10]:


b.nextnode = c


# In[11]:


a.value


# In[12]:


b.nextnode


# In[13]:


c.nextnode


# In[14]:


b.nextnode.value

