from hashtable import HashTable
from tree_intersection import tree_intersection
from trees import BinaryTree, Node
import pytest

def test_tree_insertion_happy_path():
    expected = [16, 20, 40]
    tree1 = BinaryTree()
    node1 = Node(16)
    node2 = Node(40)
    node3 = Node(25)
    node4 = Node(20)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    tree1.root = node1
    tree2 = BinaryTree()
    node1_tree2 = Node(20)
    node2_tree2 = Node(1)
    node3_tree2 = Node(40)
    node4_tree2 = Node(16)
    node1_tree2.left = node2_tree2
    node1_tree2.right = node3_tree2
    node2_tree2.left = node4_tree2
    tree2.root = node1_tree2
    actual = tree_intersection(tree1, tree2)
    assert actual == expected


def test_tree_intersection_with_empty_trees():
    with pytest.raises(Exception):
        tree1 = BinaryTree()
        tree2 = BinaryTree()
        actual = tree_intersection(tree1, tree2)


