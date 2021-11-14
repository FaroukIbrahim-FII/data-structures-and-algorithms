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


class PseudoQueue:
    def __init__(self) :
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self ,value):
        self.stack1.push(value)

    def dequeue(self):
        if self.stack1.is_empty:
            raise Exception("an empty Queue")

        while not self.stack1.is_empty:
            popped_value = self.stack1.pop()
            self.stack2.push(popped_value)


        remove = self.stack2.pop()


        while not self.stack2.is_empty:
            popped_value = self.stack2.pop()
            self.stack1.push(popped_value)

        return remove
