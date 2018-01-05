
# coding: utf-8

# In[1]:


def fib_rec(n):
    
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    else:
        return fib_rec(n-1)+fib_rec(n-2)


# In[2]:


fib_rec(10)

