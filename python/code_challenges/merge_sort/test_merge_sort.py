from merge_sort import mergesort


def test_merge_sort():
    list = [8,4,23,42,16,15]
    excpected = [4,8,15,16,23,42]
    actual = mergesort(list)
    assert actual == excpected
