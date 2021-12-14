from left_joins import left_joins
from hashtable import HashTable

def test_hashmap_left_joins_happy_path():
    first_hash_table = HashTable()
    first_hash_table.add("aaaa", "ffffff")
    first_hash_table.add("bbbb", "IIIIII")
    first_hash_table.add("cccc", "AAAAAA")
    first_hash_table.add("dddd", "XXXXXX")
    first_hash_table.add("eeee", "YYYYY")
    second_hash_table = HashTable()
    second_hash_table.add("aaaa", "zzzz")
    second_hash_table.add("cccc", "qqqq")
    second_hash_table.add("dddd", "rrrr")
    second_hash_table.add("eeee", "kkkk")

    expected = [
        ['aaaa', 'ffffff', 'zzzz'],
        ['bbbb', 'IIIIII', 'NULL'],
        ['cccc', 'AAAAAA', 'qqqq'],
        ['dddd', 'XXXXXX', 'rrrr'],
        ['eeee', 'YYYYY', 'kkkk']
        ]
    actual = left_joins(first_hash_table, second_hash_table)
    assert actual == expected


def test_hashmap_left_joins_expected_failure():
    first_hash_table = HashTable()
    second_hash_table = HashTable()


    expected = []
    actual = left_joins(first_hash_table, second_hash_table)
    assert actual == expected
