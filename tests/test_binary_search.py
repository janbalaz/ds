import pytest

from binary_search import binary_search


@pytest.mark.parametrize(
    "elem,arr,expected",
    [
        (2, [], -1),  # empty list
        (2, [1, 3, 5, 7], -1),  # not in list
        (2, [2], 0),
        (2, [2, 3, 5, 10], 0),  # first
        (12, [1, 3, 5, 9, 12], 4),  # last
        (-2, [-3, -2, -1, 0, 1, 2, 5, 9, 12], 1),  # negative numbers
        (130000, list(range(1000000)), 130000),  # bigger input
    ],
)
def test_binary_search(elem, arr, expected):
    assert binary_search(elem, arr) == expected
