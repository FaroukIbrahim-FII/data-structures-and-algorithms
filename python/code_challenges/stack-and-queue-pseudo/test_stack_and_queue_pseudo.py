from stack_and_queue_pseudo import PseudoQueue
import pytest

# Happy path
def test_enqueues_queue():
    expected = "x"
    queue = PseudoQueue()
    queue.enqueue("x")
    actual = queue.stack1.top.value
    assert expected == actual

# Happy path
def test_dequeue_queue(queue):
    expected = "w"
    actual = queue.stack1.top.value
    assert expected == actual

# Expected failure
def test_dequeue_empty_queue(queue):
    with pytest.raises(Exception, match="an empty Queue"):
        queue.dequeue()


@pytest.fixture
def queue():
    queue = PseudoQueue()
    queue.enqueue("x")
    queue.enqueue("y")
    queue.enqueue("z")
    queue.enqueue("w")

    return queue
