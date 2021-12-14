from hashtable import HashTable
from trees import BinaryTree

def tree_intersection(tree1: BinaryTree , tree2: BinaryTree) -> list:
    tree1 = tree1.in_order()
    tree2 = tree2.in_order()

    if not tree1 and not tree2:
        raise Exception("The trees are empty")
    intersected_values =[]
    hash_table = HashTable()
    for node in tree1:
        hash_table.add(str(node),node)
    for node in tree2:
        if hash_table.get(str(node)):
            intersected_values.append(node)

    if not intersected_values:
        return "no intersected values between the two trees"
    return intersected_values
