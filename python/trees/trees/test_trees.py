from trees import BinaryTree, Node , BinarySearchTree
import pytest


def test_empty_tree():
    expected = None
    tree = BinaryTree()
    actual = tree.root

    assert expected == actual


def test_tree_with_single_node():
    expected = "z"
    tree = BinaryTree()
    single_node = Node('z')
    tree.root = single_node
    actual = tree.root.data

    assert actual == expected

def test_breadth_first_test_1():
    tree = BinaryTree()
    node1 = Node('x')
    node2 = Node('y')
    node3 = Node('z')
    node4 = Node('w')
    node1.left = node2
    node1.right = node3
    node2.left = node4
    tree.root = node1
    expected = ["x", "y", "z", "w"]
    actual = tree.breadth_first()
    assert actual == expected

def test_pre_order():
    tree = BinaryTree()
    node1 = Node('x')
    node2 = Node('y')
    node3 = Node('z')
    node4 = Node('w')
    node1.left = node2
    node1.right = node3
    node2.left = node4
    tree.root = node1
    expected = ["x", "y", "w", "z"]
    actual = tree.pre_order()
    assert actual == expected

def test_post_order():
    tree = BinaryTree()
    node1 = Node('x')
    node2 = Node('y')
    node3 = Node('z')
    node4 = Node('w')
    node1.left = node2
    node1.right = node3
    node2.left = node4
    tree.root = node1
    expected = ["w", "y", "z", "x"]
    actual = tree.post_order()
    assert actual == expected

def test_in_order():
    tree = BinaryTree()
    node1 = Node('x')
    node2 = Node('y')
    node3 = Node('z')
    node4 = Node('w')
    node1.left = node2
    node1.right = node3
    node2.left = node4
    tree.root = node1
    expected = ["w", "y", "x", "z"]
    actual = tree.in_order()
    assert actual == expected



## binary search
def test_search_in_empty_tree():
   with pytest.raises(Exception):
       tree = BinarySearchTree()
       actual = tree.__contains__("O")

def test_add_left_and_right_nodes():
    tree = BinarySearchTree()
    tree.add("A")
    tree.add("B")
    tree.add("C")
    expected = ["A","B","C"]
    actual = tree.pre_order()
    assert actual == expected

def test_add_once():

    tree = BinarySearchTree()
    tree.add('A')
    expected = "A"
    actual = tree.root.data
    assert actual == expected

def test_add_twice():
    tree = BinarySearchTree()
    tree.add("A")
    tree.add("B")
    expected = ["A","B"]
    actual = tree.pre_order()
    assert actual == expected

def test_contains_value():
    tree = BinarySearchTree()
    tree.add("A")
    tree.add("B")
    tree.add("C")
    expected = True
    actual = tree.__contains__("B")
    assert actual == expected

def test_not_contains_value():
    tree = BinarySearchTree()
    tree.add("A")
    tree.add("B")
    tree.add("C")
    expected = False
    actual = tree.__contains__("z")
    assert actual == expected

