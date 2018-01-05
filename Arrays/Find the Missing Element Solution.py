
# coding: utf-8

# In[26]:


def finder(arr1, arr2):
    
    count = {}
        
    for num in arr1:
        if num in count: 
            count[num] += 1
        else:
            count[num] = 1

    for num in arr2:
        if num in count:
            count[num] -= 1
        else:
            count[num] = 1

    for number in count:
        if count[number] != 0:
            return number


# In[28]:


def finder(arr1, arr2):
    
    def sum_of_array(arr):
        sum = 0
        for num in arr:
            sum += num
        return sum
    
    if(len(arr1) > len(arr2)):
        return sum_of_array(arr1) - sum_of_array(arr2)
    
    else:
        return sum_of_array(arr2) - sum_of_array(arr1)


# In[29]:


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestFinder(object):
    
    def test(self,sol):
        assert_equal(sol([5,5,7,7],[5,7,7]),5)
        assert_equal(sol([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)
        assert_equal(sol([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
        print ('ALL TEST CASES PASSED')

# Run test
t = TestFinder()
t.test(finder)

