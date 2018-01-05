
# coding: utf-8

# In[1]:


class Node(object):
    
    def __init__(self, value):
        self.value = value
        self.nextnode = None


# In[2]:


def reverse(head):
    
    current = head
    previous = None
    next_node = None
    
    while current != None:
        
        next_node = current.nextnode
        current.nextnode = previous
        previous = current
        current = next_node


# In[3]:


# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d


# In[5]:


print (a.nextnode.value)
print (b.nextnode.value)
print (c.nextnode.value)


# In[6]:


reverse(a)


# In[7]:


print (d.nextnode.value)
print (c.nextnode.value)
print (b.nextnode.value)


# In[1]:


list1 = [1,2,3]


# In[5]:


list2 =reversed(list1)


# In[6]:



list2


# In[7]:


list2[0]


# In[8]:


list1.reverse()


# In[9]:


list1


# In[10]:


list1.join()


# In[11]:


list2 = [5, 8, 9]


# In[12]:


list1 + list2

