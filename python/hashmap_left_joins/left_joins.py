from hashtable import HashTable


def left_joins(hashmap1:HashTable, hashmap2:HashTable) -> list:

    left_joins_list = []
    for item in hashmap1:
        left_list = []
        left_list.append(item[0])
        left_list.append(item[1])
        if hashmap2.contains(item[0]):
            left_list.append(hashmap2.get(item[0]))
        else:
            left_list.append("NULL")
        left_joins_list.append(left_list)
        if item:
            item.pop(0)
            if item:
                item.pop(0)

    return left_joins_list
