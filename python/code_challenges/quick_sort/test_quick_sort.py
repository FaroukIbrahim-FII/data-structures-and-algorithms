from quick_sort import QuickSort

def test_QuickSort():
    arr = [8,4,23,42,16,15]
    expected = [4, 8, 15, 16, 23, 42]
    actual = QuickSort(arr, 0, len(arr) -1)
    assert actual == expected
