class Node:
  def __init__ (self,data,left=None,right=None):
    self.data = data
    self.left = left
    self.right = right
    self.child = []

class Queue:
  def __init__(self, collection=[]):
    self.data = collection

  def peek(self):
    if len(self.data):
      return True
    return False

  def enqueue(self,item):
    self.data.append(item)

  def dequeue(self):
    return self.data.pop(0)

class BinaryTree:

  def __init__(self):
    self.root = None

  def breadth_first(self):
    breadth = Queue()
    breadth.enqueue(self.root)

    items_list = []

    while breadth.peek():
      front = breadth.dequeue()
      items_list += [front.data]

      if front.left:
        breadth.enqueue(front.left)

      if front.right:
        breadth.enqueue(front.right)

    return items_list

  def pre_order(self):
    items_list = []
    def walk(node):
      if node:
        items_list.append(node.data)
        if node.left:
          walk(node.left)
        if node.right:
          walk(node.right)

    walk(self.root)
    return items_list

  def in_order(self):
    items_list = []
    def walk(node):
      if node:
        if node.left:
          walk(node.left)
        items_list.append(node.data)
        if node.right:
          walk(node.right)

    walk(self.root)
    return items_list

  def post_order(self):
    items_list = []
    def walk(node):
      if node:
        if node.left:
          walk(node.left)
        if node.right:
          walk(node.right)
        items_list.append(node.data)

    walk(self.root)
    return items_list

  def max_num(self):
    if not self.root:
        raise Exception("An Empty Tree")

    self.max_element=self.root.data

    def max_item(node):
        if node.data>self.max_element:
            self.max_element= node.data
        if node.left:
            max_item(node.left)
        if node.right:
            max_item(node.right)
        return self.max_element

    return max_item(self.root)

class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()

    def add(self,value):
        if not self.root:
            self.root= Node(value)
        else :
            temp = self.root
            while temp:
                if value < temp.data:
                    if not temp.left:
                        temp.left = Node(value)
                        break
                    temp = temp.left
                else:
                    if not temp.right:
                        temp.right = Node(value)
                        break
                    temp = temp.right

    def __contains__(self,value):
        if not self.root:
            raise Exception("Empty Tree !!!")

        else:
            temp = self.root
            while temp:
                if temp.data == value:
                    return True
                elif temp.data > value:
                    if not temp.left:
                        return False
                    temp = temp.left
                else:
                    if not temp.right:
                        return False
                    temp = temp.right


def breadth_first(tree):
    breadth = Queue()
    breadth.enqueue(tree.root)

    items = []

    while breadth.peek():
        front = breadth.dequeue()
        items += [front.data]

        if front.left:
            breadth.enqueue(front.left)

        if front.right:
            breadth.enqueue(front.right)

    return items


def tree_fizz_buzz(tree):
    def fizz_buzz(node):

        if not node.data % 5 and not node.data % 3 :
            return "FizzBuzz"
        elif not node.data % 3 :
            return "Fizz"
        elif not node.data % 5 :
            return "Buzz"
        else :
            return str(node.data)

    queue = Queue()
    queue.enqueue(tree.root)

    while queue.peek():
      front = queue.dequeue()
      front.data = fizz_buzz(front)

      for child in front.child:
        queue.enqueue(child)

    return tree

# this is a list generator function for testing only
def k_ary_list_gen(tree):
        breadth = Queue()
        breadth.enqueue(tree.root)

        items = []
        while breadth.peek():
            front = breadth.dequeue()
            items += [front.data]
            if front.child:
                for item in front.child:
                    breadth.enqueue(item)
        return items

# if __name__ == '__main__':
    # tree = BinaryTree()
    # node1 = Node(2)
    # node2 = Node(7)
    # node3 = Node(5)
    # node4 = Node(2)
    # node5 = Node(6)
    # node6 = Node(9)
    # node7 = Node(5)
    # node8 = Node(11)
    # node9 = Node(4)
    # node1.left = node2
    # node1.right = node3
    # node2.left = node4
    # node2.right = node5
    # node5.left = node7
    # node5.right = node8
    # node3.right = node6
    # node6.right = node9
    # tree.root = node1
    # print(breadth_first(tree))
