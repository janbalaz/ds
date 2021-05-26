from typing import List


def find_smallest(i: int, arr: List[int]) -> int:
    """
    Finds the smallest element in array starting after `i`.

    :param i: index of the current minimum
    :param arr: array of integers
    :return: position of the smallest element
    """
    smallest = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[smallest]:
            smallest = j

    return smallest


def swap_elements(i: int, j: int, arr: List[int]) -> None:
    """
    Swaps the elements in array.

    :param i: position i
    :param j: position j
    :param arr: array of integers
    """
    arr[i], arr[j] = arr[j], arr[i]


def selection_sort(arr: List[int]):
    """
    Returns sorted array using selection sort.
    Places sorted values on the left side of the array
    by swapping the smallest element with current position.

    :param arr: array of integers
    :return: sorted array of integers
    """
    for i in range(len(arr) - 1):
        j = find_smallest(i, arr)
        swap_elements(i, j, arr)

    return arr
