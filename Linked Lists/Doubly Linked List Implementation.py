
# coding: utf-8

# In[1]:


class DoublyLinkedListNode(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None
        self.prevnode = None
    


# In[2]:


a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)


# In[3]:


a.nextnode = b
b.prevnode = a


# In[4]:


b.nextnode = c
c.prevnode = b

