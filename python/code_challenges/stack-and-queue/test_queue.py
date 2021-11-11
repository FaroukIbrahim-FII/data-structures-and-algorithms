from stack_and_queue import Queue
import pytest

# Can successfully enqueue into a queue
def test_enqueues_into_queue():
    expected = "b"
    queue = Queue()
    queue.enqueue("b")
    actual = queue.rear.value
    assert expected == actual

# Can successfully enqueue multiple values into a queue
def test_multiple_enqueues_into_queue(queue):
    expected = "w"
    actual = queue.rear.value
    assert expected == actual

# Can successfully dequeue out of a queue the expected value
def test_dequeue_from_queue(queue):
    expected = "x"
    actual = queue.dequeue()
    assert expected == actual

# Can successfully peek into a queue, seeing the expected value
def test_peek_from_queue(queue):
    expected = "x"
    actual = queue.peek()
    assert expected == actual

# Can successfully empty a queue after multiple dequeues
def test_peek_from_queue_after_multiple_dequeues(queue):
    node1= queue.dequeue()
    node2= queue.dequeue()
    node3= queue.dequeue()
    node4= queue.dequeue()
    assert queue.is_empty() == True


# Can successfully instantiate an empty queue
def test_instantiate_an_empty_queue():
    queue = Queue()
    assert queue.front == None

# Calling dequeue or peek on empty queue raises exception
def test_peek_from_empty_queue():
    with pytest.raises(Exception):
        queue = Queue()
        actual = queue.peek()
        expected = "an empty Queue"
        assert actual == expected




@pytest.fixture
def queue():
    queue = Queue()
    queue.enqueue("x")
    queue.enqueue("y")
    queue.enqueue("z")
    queue.enqueue("w")

    return queue
