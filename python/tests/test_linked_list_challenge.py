# from linked_list.linked_list import Node ,LinkedList
from linked_list.linked_list_challenge import Node, LinkedList, zip_Lists


# Can successfully instantiate an empty linked list
def test_empty_linked_list():
    empty_list = LinkedList()
    expected = None
    actual = empty_list.head
    assert expected == actual

# Can properly insert into the linked list
def test_insert_linked_list():
    insert_to_list=LinkedList()
    insert_to_list.insert("x")
    added_item=insert_to_list.head
    assert added_item.value == "x"

# The head property will properly point to the first node in the linked list
def test_head():
    first_node=Node("x")
    linked_list = LinkedList()
    linked_list.head=first_node
    assert linked_list.head == first_node


# Can properly insert multiple nodes into the linked list
def test_insert_multiple_nodes():
    added_item=Node("x")
    linked_list = LinkedList()
    linked_list.head=added_item
    linked_list.insert("y")
    assert linked_list.head.value == "y"
    linked_list.insert("z")
    assert linked_list.head.value == "z"

# Will return true when finding a value within the linked list that exists
def test_include_linked_list_true():
    linked_list=LinkedList()
    linked_list.insert("x")
    excepted=True
    actual=linked_list.include("x")
    assert excepted==actual

# Will return false when searching for a value in the linked list that does not exist
def test_include_linked_list_false():
    linked_list=LinkedList()
    linked_list.insert("y")
    excepted=False
    actual=linked_list.include("x")
    assert excepted==actual

# Can properly return a collection of all the values that exist in the linked list
def test_the_whole_list():
    linked_list = LinkedList()
    item1= linked_list.insert("z")
    item2= linked_list.insert("y")
    item3= linked_list.insert("x")

    assert linked_list.__str__() == "head -> x -> y -> z -> None"

def test_append_one():
    expected = "head -> x -> y -> None"
    List = LinkedList()
    node1 = List.insert("x")
    node2 = List.append("y")
    actual = List.__str__()
    assert actual == expected


def test_insert_before():
    expected = "head -> y -> z -> x -> None"
    List = LinkedList()
    node1 = List.insert("x")
    node1 = List.insert("y")
    node2 = List.insert_before("x", "z")
    actual = List.__str__()
    assert actual == expected

def test_insert_after():
    List=LinkedList()
    node1 = List.insert("z")
    node1 = List.insert("y")
    node1 = List.insert("x")
    List.insert_after("x","a")
    List.insert_after("y","b")
    List.insert_after("z","c")
    actual=List.__str__()
    expected='head -> x -> a -> y -> b -> z -> c -> None'
    assert actual == expected

def test_k_out_of_range():
    excepted='out of range'
    List=LinkedList()
    List.insert("x")
    List.insert("y")
    List.insert("z")
    actual=List.kth_from_end(4)
    assert excepted==actual

def test_k_the_same_length():
    excepted='out of range'
    List=LinkedList()
    List.insert("x")
    List.insert("y")
    List.insert("z")
    actual=List.kth_from_end(3)
    assert excepted==actual

def test_k_negative_index():
    excepted='negative value not allowed'
    List=LinkedList()
    List.insert("x")
    List.insert("y")
    List.insert("z")
    actual=List.kth_from_end(-3)
    assert excepted==actual

def test_k_one_element():
    excepted= 'x'
    List=LinkedList()
    List.insert("x")
    actual=List.kth_from_end(1)
    assert excepted==actual

def test_zipped_lists():
     # Arrange
    excepted="head -> a -> x -> b -> y -> c -> z -> d -> None"
     # Act
    List1 =LinkedList()
    List1.insert("a")
    List1.append("b")
    List1.append("c")
    List1.append("d")

    List2 =LinkedList()
    List2.insert("x")
    List2.append("y")
    List2.append("z")
    actual= zip_Lists(List1,List2)
    #Assert
    assert excepted==actual

def test_k_happy_path():
    excepted= 'y'
    List=LinkedList()
    List.insert("x")
    List.insert("y")
    List.insert("z")
    actual=List.kth_from_end(1)
    assert excepted==actual
