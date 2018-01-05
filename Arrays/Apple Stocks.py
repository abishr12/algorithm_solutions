
# coding: utf-8

# In[27]:


high_price = {}

def highest_sell(base, end, arr):
    high_sell = -1000
    for num in range(base+1, end):
        current_sell =arr[num] - arr[base]
        if current_sell > high_sell:
            high_sell = current_sell
            
    high_price[base] = high_sell

def apple_stocks(arr):
    for i in range(0, len(arr)):
        highest_sell(i, len(arr), arr)
        
    return high_price


# In[28]:


apple_stocks([10, 7, 5, 8, 11, 9])

