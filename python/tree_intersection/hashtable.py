from trees import BinaryTree, Node
from collections import Counter

class HashTable:
    def __init__(self, size=1024):
        self.__size = size
        self.__buckets = [None] * size

    def custom_hash(self, key):
        return sum([ord(char) for char in key]) * 3 % self.__size

    def add(self, key, val):
        ind = self.custom_hash(key)
        if not self.__buckets[ind]:
          self.__buckets[ind] = BinaryTree()
        new_val = [key,val]
        node = Node(new_val)
        tree_root = self.__buckets[ind].root
        if not tree_root:
            tree_root = node
        pos_node = tree_root
        while tree_root:
            prev_pos_node = pos_node
            if not prev_pos_node.left or not prev_pos_node.right:
                pos_node = pos_node.left
                if not pos_node:
                    pos_node = node
                elif pos_node:
                    pos_node = pos_node.right
                    if not pos_node:
                        pos_node = node
                    else:
                        pos_node = pos_node.left
                        continue
                if not prev_pos_node.left:
                    prev_pos_node = prev_pos_node.left
                elif not prev_pos_node.right:
                    prev_pos_node = prev_pos_node.right

                if prev_pos_node.left and prev_pos_node.right:
                    prev_pos_node = prev_pos_node.left
                    ################ need to re-create it with a recursion ################



    def get(self, key):
      ind = self.custom_hash(key)
      if self.__buckets[ind]:
        binary_tree = self.__buckets[ind]
        current = binary_tree.root
        while current:
          if current.val[0] == key:
            return current.val[1]
          current = current.next

      return None

    def contains(self, key):
        ind = self.custom_hash(key)
        if self.__buckets[ind]:
            binary_tree = self.__buckets[ind]
            current = binary_tree.root
            while current:
                if current.val[0] == key:
                    return True
                current = current.next
            return False


def repeated_word(string: str) -> str:
    if not string:
        return "there is no input"

    # using realpython.com and GeeksforGeeks
    # splited_string = list(string.split(" "))
    # repeated = Counter(splited_string)
    # for i in splited_string:
    #     if(repeated[i] > 1):
    #         return i

    hashtabel = HashTable()
    splited_string = string.split(" ")
    for word in splited_string:
        if hashtabel.get(str(word)):
            return word
        else:
            hashtabel.add(word, word)

    return "there is no repeated word"
