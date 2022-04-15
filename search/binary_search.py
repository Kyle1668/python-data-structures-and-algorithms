def binary_search_recursive(numbers: list[int], target: int, lower: int, upper: int) -> bool:
    """Returns a boolean indicating whether a number is present in the given list

    Args:
        numbers (list[int]): The ascending ordered data set potentially containing the target number
        target (int): The number that will be queried for
        lower (int): The least most index to inspect in the sublist
        upper (int): The largest most index to inspect in the sublist

    Raises:
        ValueError: Raised if the region of the list is not sorted

    Returns:
        bool: Whether the data set contains the target nunber
    """

    midpoint_index = int((lower + upper) / 2)

    if len(numbers) is 0 or lower > upper:
        return False

    current_element = numbers[midpoint_index]

    if not is_sorted_list(numbers, midpoint_index):
        raise ValueError("The provided list is not sorted in ascending order")

    if current_element is target:
        return True

    if current_element > target:
        return binary_search_recursive(numbers, target, lower, midpoint_index - 1)

    return binary_search_recursive(numbers, target, midpoint_index + 1, upper)


def binary_search_iterative(numbers: list[int], target: int) -> bool:
    """Returns a boolean indicating whether a number is present in the given list

    Args:
        numbers (list[int]): The ascending ordered data set potentially containing the target number
        target (int): The number that will be queried for

    Raises:
        ValueError: Raised if the region of the list is not sorted

    Returns:
    bool: Whether the data set contains the target nunber
    """

    lower_index = 0
    upper_index = len(numbers)

    while lower_index <= upper_index and upper_index is not 0:
        pivot_index = int((lower_index + upper_index) / 2)

        if target is numbers[pivot_index]:
            return True

        if numbers[pivot_index] < target:
            lower_index = pivot_index + 1
            continue
        
        upper_index = pivot_index - 1


    return False


def is_sorted_list(numbers: list[int], pivot_index: int):
    """Return whether the neighbords of the current value are not ordered

    Args:
        Args:
        numbers (list[int]): The ascending ordered data set potentially containing the target number
        pivot_index (int): The index that is being used as the middle pivot

    Returns:
        _type_: Wether the neighbords of the current pivot index are sorted
    """

    pivot = numbers[pivot_index]
    valid_left = pivot_index is 0 or numbers[pivot_index - 1] <= pivot
    valid_right = pivot_index is len(numbers) - 1 or numbers[pivot_index + 1] >= pivot
    return valid_left and valid_right
