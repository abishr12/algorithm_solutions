
# coding: utf-8

# In[1]:


class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None


# In[3]:


def cycle_check(node):
    
    if(node.nextnode == None):
        return False
    
    next_node = node.nextnode
    
    while(next_node != None):
        if(next_node == node):
            return True
        next_node = next_node.nextnode
    return False


# In[4]:


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a # Cycle Here!


# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z


#############
class TestCycleCheck(object):
    
    def test(self,sol):
        assert_equal(sol(a),True)
        assert_equal(sol(x),False)
        
        print ("ALL TEST CASES PASSED")
        
# Run Tests

t = TestCycleCheck()
t.test(cycle_check)

