
# coding: utf-8

# In[11]:


def get_max_profit(arr):

    min_price = arr[0]
    answer = arr[1] - arr[0]
    
    for price in arr:
        
        current_price = price
        print(current_price)
        
        min_price = min(current_price, min_price)
        print(min_price)
        output = current_price - min_price
        
        
        if output > answer:
            
            answer = output
        
        
    
    return answer


# In[12]:


stock_prices_yesterday = [11, 9, 6, 3, 1]

get_max_profit(stock_prices_yesterday)
# returns 6 (buying for $5 and selling for $11)

