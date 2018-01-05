
# coding: utf-8

# In[1]:


def get_shortest_unique_substring(arr, str):

  L = [] # keep track of all the smallest substrings
  
  min_string=""
  
  for index in range(len(str)):
    new_str = str[index:]
    answer = ""
    dict_set = set()
    
    
    num_unique_letters = 0
    
    for letter in new_str:
      answer = answer + letter
      
      if letter in arr:
          dict_set.add(letter)
        
      if (len(dict_set) == len(arr)):
        L.append(answer)
        break
    
    
  if len(L) == 0:
    return min_string
  else:
    min_string = L[0]
    
  for string in L:
    
    if len(string) < len(min_string):
      min_string = string
      
  
  return min_string
    



# In[ ]:


def get_shortest_unique_substring(arr, str):
  m = len(arr)
  result = "" #current best
  count = 0 # number of unique chars that our substring contains
  
  char_count = {} # count for each char in arr that are in our substring
  for a in arr:
    char_count[a] = 0
  head = 0
  
  for tail in range(0, len(str)):
    #if substring from head to tail does not contain all the character then push tail further
    c_tail = str[tail]
    if c_tail in char_count:
      if char_count[c_tail] == 0:
        count += 1 # a new unique character has been detected
      
      char_count[c_tail]+=1
    else:
      continue
      
    while (count == m):
         # count = m so advance the head
      if (tail - head + 1) == m:
        return str[head:tail+1]
    
      # update current best string
      if (result == "") or (tail - head + 1) < len(result):
        result = str[head:tail+1]
      
      c_head = str[head]
      if c_head in char_count:
        char_count[c_head] -= 1
        if char_count[c_head] == 0:
          count -= 1
          
      head += 1
  
  return result

