from stack_and_queue import Stack
import pytest


# Can successfully push onto a stack
def test_push_onto_a_stack(stack):
    expected = "w"
    actual = stack.top.value
    assert expected == actual

# Can successfully push multiple values onto a stack
def test_push_multiple_values_onto_a_stak():
    expected = "x"
    stack = Stack()
    stack.push("x")
    actual = stack.top.value
    assert expected == actual

# Can successfully pop off the stack
def test_pop_off_the_stack(stack):
    expected = "w"
    actual = stack.pop()
    assert expected == actual

# Can successfully empty a stack after multiple pops
def test_pop_empty_a_stack(stack):
    node1 = stack.pop()
    node2 = stack.pop()
    node3 = stack.pop()
    node4 = stack.pop()
    assert stack.is_empty() == True


# Can successfully peek the next item on the stack
def test_peek_next_item_on_the_stack(stack):
    expected = "w"
    actual = stack.peek()
    assert expected == actual

# Can successfully instantiate an empty stack
def test_instantiate_an_empty_stack():
    stack = Stack()
    assert stack.is_empty() == True

# Calling pop or peek on empty stack raises exception
def test_peek_from_empty_stack():
    with pytest.raises(Exception):
        stack = Stack()
        actual = stack.peek()
        expected = "You can't pop an empty stack"
        assert actual == expected



@pytest.fixture
def stack():
    stack = Stack()
    stack.push("x")
    stack.push("y")
    stack.push("z")
    stack.push("w")

    return stack
