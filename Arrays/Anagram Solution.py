
# coding: utf-8

# In[9]:


def anagram(str1, str2):
    
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    count = {}
    
    if len(str1) != len(str2):
        return False
    
    for char in str1:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
            
    for char in str1:
        if char in count:
            count[char] -= 1
        else:
            count[char] = 1
    
    for key in count:
        if count[key] != 0:
            return False
    
    return True
            


# In[10]:


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class AnagramTest(object):
    
    def test(self,sol):
        assert_equal(sol('go go go','gggooo'),True)
        assert_equal(sol('abc','cba'),True)
        assert_equal(sol('hi man','hi     man'),True)
        assert_equal(sol('aabbcc','aabbc'),False)
        assert_equal(sol('123','1 2'),False)
        print ("ALL TEST CASES PASSED")

# Run Tests
t = AnagramTest()
t.test(anagram)


# In[4]:


count = {}


# In[5]:


count[5]


# In[6]:


count['g']

