# Implement a Stack
#
# A very common interview question is to begin by just implementing a Stack! Try your best to implement your own stack!
#
# It should have the methods:
#
# Check if its empty
# Push a new item
# Pop an item
# Peek at the top item
# Return the size

class Stack (object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, obj):
        self.items.append(obj)

    def peek(self):
        return self.items[-1]

    def pop(self):
        return self.items[-1]
        self.items = self.items[:len(self.items)-2]

    def size(self):
        return len(self.items)
