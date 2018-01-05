
# coding: utf-8

# Dynamic Array Implementation

# In[8]:


import ctypes

class DynamicArray(object):
    
    def __init__(self):
        
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)
        
    def __len__(self):
        return self.n
    
    def __getitem__(self, k):
        
        if not 0<= k < self.n:
            return IndexError('K out of bounds!')
        
        return self.A[k]
    
    def capacity(self):
        return self.capacity
    
    def append(self, ele):
        
        if self.n == self.capacity:
            self._resize(2*self.capacity) #2x if capacity isn't 
        
        self.A[self.n]= ele
        self.n += 1
        print ("After appending, new size is ", ctypes.sizeof(self.A))
        
    def _resize(self, new_cap):
        
        B = self.make_array(new_cap)
        
        for k in range(self.n):
            B[k] = self.A[k]
            
        self.A = B
        self.capacity = new_cap
        
    def make_array(self, new_cap):
        
        return (new_cap * ctypes.py_object)()


# In[9]:


arr = DynamicArray()


# In[10]:


arr.append(1)


# In[11]:


len(arr)


# In[12]:


getitem(0)


# In[17]:


arr.__getitem__(0)


# In[18]:


arr.__len__()


# In[19]:


getitem(0)


# In[20]:


getitem(arr,0)

