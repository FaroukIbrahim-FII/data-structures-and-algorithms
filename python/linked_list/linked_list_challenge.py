class Node:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)
        if self.head != None:
            node.next = self.head
        self.head = node

    def include(self,value):
        if self.head is None:
            return False
        else:
            current =self.head
            while current is not None:
                if current.value == value:
                    return True
                current = current.next
            return False

    def __str__(self):
        output = "head -> "
        if self.head is None:
            output += None
        else:
            current = self.head
            while(current):
                output += f"{current.value} -> "
                current = current.next
            output += "None"
            return output

