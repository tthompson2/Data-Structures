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
            if self.left != None:
                found = True
                return found
            else:
                self.left.contains(target)

        if target >= self.value:
            if self.right != None:
                found = True
                return found
            else: 
                self.right.contains(target)


    
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()  

    def for_each(self, fn):
        if self.left != None:
            self.left.for_each(fn)

        fn(self.value) # why doe

        if self.right != None:
            self.right.for_each(fn)
        

    def in_order_print(self, node):
        if self.left is None and self.right is None:
            print(self.value)
        if self.left != None:
            self.left.in_order_print(node)
        if self.right != None:
            self.right.in_order_print(node)

    def bft_print(self, node):
        pass

    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass