import unittest
class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node
  

class LinkedList:
  def __init__(self):
    # Stores a node, that corresponds to our first node in the list 
    self.head = None     
    # stores a node that is the end of the list
    self.tail = None 
  
  # return all values in the list a -> b -> c -> d -> None
  def __str__(self):
    output = ''
    current_node = self.head # create a tracker node variable
    while current_node is not None: # loop until its NONE

      output += f'{current_node.value} -> '

      current_node = current_node.next_node # update the tracker node to the next node

    return output
  def add_to_head(self, value):
    # create a node to add
    new_node = Node(value)
    # check if list is empty
    if self.head is None and self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      # new_node should point to current head
      new_node.next_node = self.head
      # move head to new node
      self.head = new_node

  def add_to_tail(self, value):
    # create a node to add
    new_node = Node(value)
    # check if list is empty
    if self.head is None and self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      # point the node at the current tail, to the new node
      self.tail.next_node = new_node
      self.tail = new_node

  # remove the head and return its value
  def remove_head(self):
    # if list is empty, do nothing
    if not self.head:
      return None
    # if list only has one element, set head and tail to None
    if self.head.next_node is None:
      head_value = self.head.value
      self.head = None
      self.tail = None
      return head_value
    # otherwise we have more elements in the list
    head_value = self.head.value
    self.head = self.head.next_node
    return head_value 

  def contains(self, value):
    if self.head is None:
      return False
    
    # Loop through each node, until we see the value, or we cannot go further
    current_node = self.head

    while current_node is not None:
      # check if this is the node we are looking for
      if current_node.value == value:
        return True

      # otherwise, go to the next node
      current_node = current_node.next_node
    return False 

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        # add an element to the front of our array
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        # check if empty
        if self.size == 0:
            return None
        # remove the first element in storage
        self.size -= 1
        node = self.storage.remove_head()
        return node