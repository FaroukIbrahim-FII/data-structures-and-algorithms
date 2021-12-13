from hashtable import HashTable, repeated_word
import pytest


def test_add_to_your_hash_table(hashtable):
    expected = "55"
    hashtable.add("FII","55")
    actual = hashtable.get("FII")
    assert actual == expected

def test_retrieving_based_on_key(hashtable):
    expected = "bee"
    hashtable.add("bee","bee")
    actual = hashtable.get("bee")
    assert actual == expected

def test_returns_null_for_a_non_exist_key(hashtable):
    expected = None
    actual = hashtable.get("ffffffff")
    assert actual == expected


def test_handle_collision_within_hash_table(hashtable):
    expected = "55"
    hashtable.add("FII","50")
    hashtable.add("FII","55")
    actual = hashtable.get("FII")
    assert actual == expected

def test_retrieving_value_within_a_hash_table_that_has_collision(hashtable):
    expected = "55"
    hashtable.add("FII","60")
    hashtable.add("FII","55")
    actual = hashtable.get("FII")
    assert actual == expected

def test_repeated_word():
    actual = repeated_word("Once upon a time, there was a brave princess who...")
    expected = "a"
    assert actual == expected



###########Pytest Fixture#############

@pytest.fixture
def hashtable():
	return HashTable()
