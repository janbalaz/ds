import pytest

from selection_sort import find_smallest, selection_sort, swap_elements


@pytest.mark.parametrize(
    "i,arr,expected",
    [
        (0, [], 0),
        (0, [3, 2, 12], 1),
        (0, [1, 2, 12], 0),  # min is the first
        (2, [1, 2, 12, 3, 5], 3),  # partially sorted
    ],
)
def test_find_smallest(i, arr, expected):
    assert find_smallest(i, arr) == expected


@pytest.mark.parametrize(
    "i,j,arr,expected",
    [
        (3, 3, [14, 2, 4, 5, 7], [14, 2, 4, 5, 7]),  # identical
        (1, 4, [13, 2, 15, 66, 67, 89], [13, 67, 15, 66, 2, 89]),
    ],
)
def test_swap_elements(i, j, arr, expected):
    swap_elements(i, j, arr)
    assert arr == expected


@pytest.mark.parametrize(
    "arr,expected",
    [
        ([], []),
        ([2], [2]),
        ([2, 1], [1, 2]),
        ([1, 2, 3], [1, 2, 3]),
        ([30, 13, 0, 2, 1, 70], [0, 1, 2, 13, 30, 70]),
        ([30, -13, 0, -2, 1, 70], [-13, -2, 0, 1, 30, 70]),
    ],
)
def test_selection_sort(arr, expected):
    assert selection_sort(arr) == expected
