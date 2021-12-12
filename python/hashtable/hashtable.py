from linked_list import LinkedList

class HashTable:
    def __init__(self, size=1024):
        self.__size = size
        self.__buckets = [None] * size

    def custom_hash(self, key):
        return sum([ord(char) for char in key]) * 3 % self.__size

    def add(self, key, val):
        ind = self.custom_hash(key)
        if not self.__buckets[ind]:
          self.__buckets[ind] = LinkedList()
        new_val = [key,val]
        self.__buckets[ind].insert(new_val)

    def get(self, key):
      ind = self.custom_hash(key)
      if self.__buckets[ind]:
        linked_list = self.__buckets[ind]
        current = linked_list.head
        while current:
          if current.val[0] == key:
            return current.val[1]
          current = current.next

      return None

    def contains(self, key):
        ind = self.custom_hash(key)
        if self.__buckets[ind]:
            linked_list = self.__buckets[ind]
            current = linked_list.head
            while current:
                if current.val[0] == key:
                    return True
                current = current.next
            return False
