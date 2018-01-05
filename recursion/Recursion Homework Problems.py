
# coding: utf-8

# In[1]:


def rec_sum(n):
    
    if n == 1:
        return 1
    
    else:
        return n + rec_sum(n-1)


# In[2]:


rec_sum(4)


# In[3]:


def sum_func(n):
    
    if n % 10 == n:
        return n
    
    else:
        return n%10 + sum_func(n//10)


# In[4]:


sum_func(5893)


# In[5]:


def word_split(phrase,list_of_words, output = None):
    '''
    Note: This is a very "python-y" solution.
    ''' 
    
    # Checks to see if any output has been initiated.
    # If you default output=[], it would be overwritten for every recursion!
    if output is None:
        output = []
    
    # For every word in list
    for word in list_of_words:
        
        # If the current phrase begins with the word, we have a split point!
        if phrase.startswith(word):
            
            # Add the word to the output
            output.append(word)
            
            # Recursively call the split function on the remaining portion of the phrase--- phrase[len(word):]
            # Remember to pass along the output and list of words
            return word_split(phrase[len(word):],list_of_words,output)
    
    # Finally return output if no phrase.startswith(word) returns True
    return output        


# In[6]:


word_split('themanran',['the','ran','man'])


# In[7]:


s= 'hello'


# In[8]:


s.pop()


# In[26]:


def rec_coin_dynam(target, coins, cache):
    
    min_coins = target
    
    if target in coins:
        cache[target]= 1
        return 1
    
    elif cache[target] > 0:
        return cache[target]
    
    else:
        
        for coin in [c for c in coins if c <= target]:
            
            number_coins = 1 + rec_coin_dynam(target-coin, coins, cache)
            
            if(number_coins < min_coins):
                cache[target] = number_coins
                min_coins = number_coins
    
    return min_coins


# In[27]:


target = 74
coins = [1,5,10,25]
known_results = [0]*(target+1)

rec_coin_dynam(target,coins,known_results)


# In[28]:


new_cache = [0] * 50


# In[29]:


new_cache[49]

