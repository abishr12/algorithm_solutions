
# coding: utf-8

# In[6]:


def compress(s):
    
    count = {}
    result = ""
    
    for letter in s:
        
        if letter not in count:
            count[letter] = 1
        else:
            count[letter] += 1
            
    for key in count:
        result += str(key) 
        result += str(count[key])
    
    return result


# In[10]:


compress('AAAAAaaaCCCCA')


# In[8]:


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print ('ALL TEST CASES PASSED')

# Run Tests
t = TestCompress()
t.test(compress)

