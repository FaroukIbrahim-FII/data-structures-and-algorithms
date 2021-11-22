class Node:
    def __init__(self, value, next_ = None):
        self.value = value
        self.next = next_
    def __str__(self):
        return f"{self.value}"

class EmptyStack(Exception):
    """Exception raised when pop or peek from empty stack.
    """

    def init(self,value, message="empty stack"):
        self.value = value
        self.message = message
        super().init(self.message)

    def str(self):
        return f'cant pop or peek "{self.value}" from {self.message}'


class Stack:
    def __init__(self):
        self.top = None

    def push(self,value):
        """ push value to the top of stack
        """
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """ remove the top of stack and return its value
        """

        if self.is_empty():
            raise EmptyStack(self.top)
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.value

    def peek(self):
        """ return the top value from the stack
        """

        if self.is_empty():
            raise EmptyStack(self.top)
        return self.top.value

    def is_empty(self):
        """ check if the stack is empty
        """
        return self.top == None
    def __str__(self):
        """ print stack
        """
        str_stack = f"{{{self.top}}} <-- Top"
        temp = self.top
        while temp.next:
            str_stack = f"{{{temp.next.value}}} <-- " + str_stack
            temp = temp.next
        str_stack= f"NULL <-- "+ str_stack
        return str_stack


def getMax(stack):
    temp = stack.top
    maxStack =temp.value
    while temp.next:
        temp = temp.next
        if temp.value > maxStack:
            maxStack = temp.value
    return maxStack

if __name__=="__main__":
    stack = Stack()
    stack.push(100)
    stack.push(10000)
    stack.push(50)
    stack.push(2)

    # print(stack.__str__())
    print(getMax(stack))



