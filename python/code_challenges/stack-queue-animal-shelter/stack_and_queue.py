class Node:
  def __init__(self, value, next_ = None):
    self.value = value
    self.next = next_


class Stack:
    def __init__(self) :
       self.top = None

    def push(self ,value):
        node=Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if not self.top :
            raise Exception("You can't pop an empty stack")
        else :
           temp = self.top
           self.top = self.top.next
           temp.next = None
        return temp.value

    def peek(self):
        if not self.top :
            raise Exception("an empty stack")
        else :
            return self.top.value

    def is_empty(self):
        if not self.top:
            return True
        return False

class Queue:
    def __init__(self) :
       self.front = None
       self.rear = None

    def enqueue(self ,value):
        node = Node(value)
        if not self.rear:
           self.front = node
           self.rear= node
        else :
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if not self.front :
            raise Exception("an empty queue")
        else :
            temp = self.front
            self.front = self.front.next
            temp.next = None

        return temp.value

    def peek(self):
        if not self.front :
            raise Exception("an empty Queue")
        else :
            return self.front.value

    def is_empty(self):
        if not self.front:
            return True
        return False
