
# coding: utf-8

# In[2]:


def large_cont_sum (arr):
    
    count = {} 
    max_value = arr[0]
    
    def sum_from_start(start, stop , array):
        end = inc = start
        new_sum = 0
        old_sum = 0
        
        while inc < stop:
            new_sum += array[inc]
            if(new_sum > old_sum):
                end = inc
                old_sum = new_sum
            inc += 1
        
        count[start, end] = old_sum 
    
    for number in range(len(arr)):
        sum_from_start(number, len(arr), arr)
    
    for key in count:
        if(count[key]> max_value):
            max_value = count[key]
            max_keys = key
    
    return max_keys, max_value
 
    
            
    
           


# In[3]:


from nose.tools import assert_equal

class LargeContTest(object):
    def test(self,sol):
        assert_equal(sol([1,2,-1,3,4,-1]),9)
#        assert_equal(sol([1,2,-1,3,4,10,10,-10,-1]),29)
#        assert_equal(sol([-1,1]),1)
        print ('ALL TEST CASES PASSED')
        
#Run Test
t = LargeContTest()
t.test(large_cont_sum)

