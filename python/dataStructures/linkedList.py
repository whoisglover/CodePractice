# Linked list is like a train, seperate cars are attached to each other in a row.
# Data is held in 'nodes', each node has a piece of data and a pointer to the next node in the list
# Head is the front of the list, back of the list will point to None for next node
# Methods:
# Insert:Inserts a new node into the list
# Search: Searches for a node in the list, returns node if found or false if not
# Size: Returns size of linked list
# Delete: Takes a node as an argument and deletes if it exists in the list

class Node(object):
  def __init__(self, data):
    self.data = data
    self.nextNode = None

class linkedList(object):
    def __init__(self, head=None):
    self.head = head
    self.size = 0
# Insert, put a new node at head, point its next to the previous head. Constant time insertion
  def insert(self, node):
    if not self.head:
      self.head = node
      self.size += 1
    else:
      # set new nodes pointer to old head
      node.next = self.head
      # reset head to new node
      self.head = node
      self.size += 1

# Search - recursive - Check if the head is the node you are looking for, if yes return it, if not call search again with the next node as head, if there is no next node return false.Time complexity is O(n) worst case you might have to check every node. Space complexity is worst bc on each call a new list is created with size n-1
  def search(self, lList, Node):
    if self.head == Node:
      return self.head
    else:
      if lList.head.nextNode:
        self.search(linkedList(lList.head.nextNode), Node)
      else:
        raise ValueError("Node not in Linked List")

# Size - iterate through the list and increment size counter, return at the end. Time complexity O(n) must touch each node.

  def size(self):
    current = self.head
    size = 0
    while current is not None:
      size += 1
      current = current.nextNode
    return size

# Delete - search for given node. Once it is found make the previous node's nextNode point to the node after the to-be-deleted node. Give error if list size is 0.

  def delete(self, node):
    if self.size == 0:
      raise ValueError("List is empty - nothing to delete.")
    else:
      current = self.head
      previous = None
      found = False
      while not found:
        if current == node:
          found = True
        elif current is None:
          raise ValueError("Node not found in the linked list.")
        else:
          previous = current
          current = current.nextNode
      if previous is None:
        self.head = current.nextNode
      else:
        # actual deletion happening here
        previous.nextNode = current.nextNode

myList = linkedList()
myNode = Node(4)
myNode2 = Node(2)

myList.insert(Node(5))
print myList.size()
myList.insert(myNode2)
print myList.head.data
print myList.head.nextNode

# print size(myList)