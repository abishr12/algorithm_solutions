
# coding: utf-8

# In[4]:


class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode  = None


# In[5]:


def nth_to_last_node(n, head):
    
    current = head
    position = {}
    index = 1
    
    while current != None:
        
        position[current] = index
        current= current.nextnode
        index += 1

#     return position
    
    for node in position:
        if position[node] == (len(position)+1-n):
            return node


# In[6]:


"""
RUN THIS CELL TO TEST YOUR SOLUTION AGAINST A TEST CASE 

PLEASE NOTE THIS IS JUST ONE CASE
"""

from nose.tools import assert_equal

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

####

class TestNLast(object):
    
    def test(self,sol):
        
        assert_equal(sol(2,a),d)
        print ('ALL TEST CASES PASSED')
        
# Run tests
t = TestNLast()
t.test(nth_to_last_node)


# In[8]:




