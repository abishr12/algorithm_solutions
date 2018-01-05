
# coding: utf-8

# In[1]:


class BinaryTree(object):
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key


# In[2]:


a = BinaryTree(70)


# In[3]:


a.insertRight(93)


# In[4]:


a.insertLeft(31)


# In[5]:


a.getRightChild().insertLeft(73)


# In[6]:


a.getRightChild().insertRight(94)


# In[7]:


a.getLeftChild().insertLeft(14)


# In[8]:


a.getLeftChild().getLeftChild().insertRight(23)


# In[9]:


def preorder(tree):
    
    if tree: 
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


# In[10]:


def postorder(tree):
    
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())


# In[11]:


def inorder(tree):
    
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())


# In[12]:


preorder(a)


# In[13]:


postorder(a)


# In[14]:


inorder(a)

