from left_joins import left_joins
from hashtable import HashTable

def test_hashmap_left_joins_happy_path():
    hashmap1 = HashTable()
    hashmap1.add("aaaa", "ffffff")
    hashmap1.add("bbbb", "IIIIII")
    hashmap1.add("cccc", "AAAAAA")
    hashmap1.add("dddd", "XXXXXX")
    hashmap1.add("eeee", "YYYYY")
    hashmap2 = HashTable()
    hashmap2.add("aaaa", "zzzz")
    hashmap2.add("cccc", "qqqq")
    hashmap2.add("dddd", "rrrr")
    hashmap2.add("eeee", "kkkk")

    expected = [
        ['aaaa', 'ffffff', 'zzzz'],
        ['bbbb', 'IIIIII', 'NULL'],
        ['cccc', 'AAAAAA', 'qqqq'],
        ['dddd', 'XXXXXX', 'rrrr'],
        ['eeee', 'YYYYY', 'kkkk']
        ]
    actual = left_joins(hashmap1, hashmap2)
    assert actual == expected

def test_hashmap_left_joins_expected_failure_without_the_first_map():
    hashmap1 = HashTable()
    hashmap2 = HashTable()
    hashmap2.add("aaaa", "zzzz")
    hashmap2.add("cccc", "qqqq")
    hashmap2.add("dddd", "rrrr")
    hashmap2.add("eeee", "kkkk")


    expected = []
    actual = left_joins(hashmap1, hashmap2)
    assert actual == expected


def test_hashmap_left_joins_expected_failure():
    hashmap1 = HashTable()
    hashmap2 = HashTable()


    expected = []
    actual = left_joins(hashmap1, hashmap2)
    assert actual == expected
