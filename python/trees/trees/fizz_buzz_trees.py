class Node:
    def __init__(self,value):
        self.value = value
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,value):
        new_node=Node(value)
        if not self.rear :
            self.rear=new_node
            self.front=new_node
        else:
            self.rear.next=new_node
            self.rear=new_node

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Empty queue")
        else:
            temp=self.front
            self.front=self.front.next
            temp.next=None
        if self.front==None: # if size of queue is 1
            self.rear=None
        return temp.value
    def isEmpty(self):
        if self.front is None and self.rear is None:
            return True
        else:
            return False
    def peek(self):
        if self.isEmpty():
            raise Exception("Empty queue")
        else:
            return self .front.value


class TreeNode:
    def __init__(self,data=None,children=[]):
        self.data = data
        self.children = children


class K_Ary_Tree:
    def __init__(self,root=None):
        self.root = root

    def breadth_first(self):
        queue =Queue()
        queue_output = []


        queue.enqueue(self.root)

        while not queue.isEmpty():
            front=queue.dequeue()

            for child in front.children:
                queue.enqueue(child)
            queue_output.append(front.data)
        return queue_output



def fizz_buzz_tree(k_ary_tree : K_Ary_Tree):

    def fizz_buzz(node):

        if not node % 5 and not node % 3:
            return "Fizz_Buzz"
        elif not  node % 3 :
            return "Fizz"
        elif not node % 5:
            return "Buzz"
        else:
            return str(node)


    if not k_ary_tree.root:
        return 'Empty Tree'

    queue = Queue()
    queue.enqueue(k_ary_tree.root)

    while not queue.isEmpty():
        front=queue.dequeue()
        front.data = fizz_buzz(front.data)
        for child in front.children:
            queue.enqueue(child)

    return k_ary_tree
