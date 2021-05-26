def binary_search(elem, arr):
    """
    Searches for the `elem` position in `arr`.

    :param elem: an element which we search for in `arr`
    :param arr: a sorted list of integers
    :return: position of `elem` in `arr` or `-1` if not found
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (low + high) // 2

        if arr[middle] == elem:
            return middle

        if arr[middle] < elem:
            # search in the higher numbers
            low = middle + 1
        else:
            # search in the lower numbers
            high = middle - 1

    return -1
