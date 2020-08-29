"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 
This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from queue import Queue
from stack import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left != None: 
                self.left.insert(value)
            else: 
                self.left = BSTNode(value) 

        if  value >= self.value:
            if self.right != None:
                self.right.insert(value)
            else:
                self.right = BSTNode(value) 
        pass

    def contains(self, target):
        found = False

        if target < self.value:
            if self.left is None:
                if target == self.value:
                    found = True
                    return found
                else:
                    return found
            else:
                return self.left.contains(target)

        if target >= self.value:
            if self.right is None:
                if target == self.value:
                    found = True
                    return found
                else: 
                    return found
            else: 
                return self.right.contains(target)
    
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()  

    def for_each(self, fn):
        if self.left != None:
            self.left.for_each(fn)

        fn(self.value) 

        if self.right != None:
            self.right.for_each(fn)
        

    def in_order_print(self, node):
        if self.left != None:
            self.left.in_order_print(node)
        print(self.value)
        if self.right != None:
            self.right.in_order_print(node)

    def bft_print(self, node):
        queue = Queue()

        queue.enqueue(self)

        while queue is not None:
            # current_node = 
            queue.dequeue(self, node)
            print(current_node)
            queue.enqueue(self.left)
            queue.enqueue(self.right)

        # if self.left is None and self.right is None:
        #     queue.dequeue(self)
        #     print(self.value)
        # else:
        #     queue.enqueue(self)
        #     queue.enqueue(self.left)
        #     queue.enqueue(self.right)

    def dft_print(self, node):
        stack = Stack()
        if self.left is not None and self.right is not None:
            stack.push(self)
        else:
            print(self.value)
            stack.pop(self)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(self.value)
        if self.left != None:
            self.left.in_order_print(node)
        if self.right != None:
            self.right.in_order_print(node)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if self.left != None:
            self.left.in_order_print(node)
        if self.right != None:
            self.right.in_order_print(node)
        print(self.value)