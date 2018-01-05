
# coding: utf-8

# In[3]:


def uni_char(s):

    if len(s) > 26:
        return False
    
    letters= []
    
    for char in s:
        if char not in letters:
            letters.append(char)
        else:
            return False
        
        
    return True


# In[4]:


"""
RUN THIS CELL TO TEST YOUR CODE>
"""
from nose.tools import assert_equal


class TestUnique(object):

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print ('ALL TEST CASES PASSED')
        
# Run Tests
t = TestUnique()
t.test(uni_char)

