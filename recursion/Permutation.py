
# coding: utf-8

# In[45]:


def permute(s):
    out = []
    
    # Base Case
    if len(s) == 1:
        out = [s]
        
    else:
        # For every letter in string
        for i, let in enumerate(s):
            
            print('slice is ', s[:i] + s[i+1:])
            # For every permutation resulting from Step 2 and 3 described above
            for perm in permute(s[:i] + s[i+1:]):
                
                print('perm is ', perm)
                
                print('let + perm is '+ let + perm)
                # Add it to output
                out += [let + perm]

    return out


# In[46]:


permute('abc')


# In[38]:


for i , let  in enumerate('abc'):
    print(i , let)


# In[1]:


out = [b]


# In[2]:


out = ['b']

