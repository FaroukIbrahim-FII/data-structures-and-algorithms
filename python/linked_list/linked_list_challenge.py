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

    def append(self, new_value):
        node = Node(new_value)
        current = self.head
        if current == None:
            current = node
        else:
            while current.next != None:
                current = current.next
        current.next = node

    def insert_before(self, value, new_value):
        node = Node(new_value)
        current_node = self.head
        if current_node.value is value:
            node.next = self.head
            self.head = node
        else:
            while current_node.next:
                if current_node.next.value is value:
                    node.next = current_node.next
                    current_node.next = node
                    break
                current_node = current_node.next

    def insert_after(self, value, new_value):
        current = self.head
        while current is not None:
            if current.value is value:
                break
            current = current.next
        if current is None:
            raise Exception(" there is no value ")
        else:
            new_node = Node(new_value)
            new_node.next = current.next
            current.next = new_node


    def kth_from_end(self, k):
        current = self.head
        list_length = 1
        while current.next:
            list_length += 1
            current = current.next
        current = self.head
        if k < 0:
            return 'negative value not allowed'
        elif k >= list_length and k != 1:
            return 'out of range'
        elif k == 1 and list_length == 1:
            return current.value
        value = list_length-k-1
        for i in range(list_length):
            if i == value:
                return current.value
            current = current.next


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

