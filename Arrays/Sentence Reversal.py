
# coding: utf-8

# In[28]:


def rev_word(s):
    
    s= s.strip()
    arr_words = s.split()
    answer = ""
    
    if len(arr_words) == 1:
        return arr_words[0]
    
    for num in range(len(arr_words)-1,-1,-1):
        answer += arr_words[num] + " "
        
    answer = answer.strip()
    
    return answer

rev_word('    space before')


# In[31]:


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""

from nose.tools import assert_equal

class ReversalTest(object):
    
    def test(self,sol):
        assert_equal(sol('    space before'),'before space')
        assert_equal(sol('space after     '),'after space')
        assert_equal(sol('   Hello John    how are you   '),'you are how John Hello')
        assert_equal(sol('1'),'1')
        print ("ALL TEST CASES PASSED")
        
# Run and test
t = ReversalTest()
t.test(rev_word)


# In[1]:


list = ['a', 'b', 'c']


# In[2]:


"".join(list)


# In[3]:


list = [5, 8, 9]


# In[4]:


"".join(list)


# In[5]:


num = 842


# In[6]:


list(num)


# In[7]:


list("happy")


# In[8]:


list1 = list("happy")

