
# coding: utf-8

# In[9]:


def reverse(s):
    
    if len(s) == 1:
        return s
    
    else:
        return s[-1] + reverse(s[:-1])


# In[10]:


reverse('abc')


# In[11]:


s = 'abc'


# In[12]:


s[-1]


# In[1]:


my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list):
    print(c, value)

