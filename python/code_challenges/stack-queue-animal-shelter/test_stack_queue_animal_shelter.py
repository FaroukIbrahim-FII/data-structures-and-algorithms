from stack_queue_animal_shelter import AnimalShelter
import pytest

# Happy path
def test_enqueue_cat():
    expected = "cat"
    animal_shelter=AnimalShelter()
    animal_shelter.enqueue_animal("cat")
    actual = animal_shelter.cat.rear.value

    assert expected == actual

# Happy path
def test_enqueues_dog():
    expected = "dog"
    animal_shelter=AnimalShelter()
    animal_shelter.enqueue_animal("dog")
    actual = animal_shelter.dog.rear.value

    assert expected == actual

# Expected failure
def test_enqueues_other():
    with pytest.raises(Exception):
        animal_shelter=AnimalShelter()
        animal_shelter.enqueue_animal("duck")


# Happy path
def test_dequeues_dog():
    expected = "dog2"
    animal_shelter=AnimalShelter()
    animal_shelter.enqueue_animal("dog1")
    animal_shelter.enqueue_animal("dog2")
    animal_shelter.dequeue_animal("dog1")
    actual = animal_shelter.dog.front.value

    assert expected == actual

# Happy path
def test_dequeues_cat():
    expected = "cat2"
    animal_shelter=AnimalShelter()
    animal_shelter.enqueue_animal("cat1")
    animal_shelter.enqueue_animal("cat2")
    animal_shelter.dequeue_animal("cat1")
    actual = animal_shelter.cat.front.value

    assert expected == actual
# Expected failure
def test_dequeues_other():
    expected = "null"
    animal_shelter=AnimalShelter()
    actual= animal_shelter.dequeue_animal("duck")

    assert expected == actual
