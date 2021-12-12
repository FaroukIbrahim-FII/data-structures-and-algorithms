class Node:
    def __init__(self, val=None, next_=None):
        self.val = val
        self.next = next_


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        self.head = Node(val, self.head)
