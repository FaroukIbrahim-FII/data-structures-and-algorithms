from insertion_sort import insertionSort

def test_selection_sort():
    actual = insertionSort([8, 4, 23, 42, 16, 15])
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected
