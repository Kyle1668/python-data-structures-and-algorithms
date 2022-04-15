import pytest
from binary_search import binary_search_recursive, binary_search_iterative

problem_space = [-1, 5, 88, 303, 1999, 2000]


def test_binary_search_recursive_contains_target_left_side():
    assert binary_search_recursive(problem_space, 5, 0, len(problem_space)) == True


def test_binary_search_recursive_contains_target_midpoint():
    assert binary_search_recursive(problem_space, 303, 0, len(problem_space)) == True


def test_binary_search_recursive_contains_right_side():
    assert binary_search_recursive(problem_space, 2000, 0, len(problem_space)) == True


def test_binary_search_recursive_not_contains_target():
    assert binary_search_recursive(problem_space, 100, 0, len(problem_space)) == False


def test_binary_search_recursive_empty_input():
    assert binary_search_recursive([], 1, 0, 0) == False


def test_binary_search_recursive_unsortedlist_throws_exception():
    unsorted_problem_space = [-1, 200, 88, 303, 10, 2000]

    with pytest.raises(ValueError):
        assert binary_search_recursive(unsorted_problem_space, -1, 0, len(unsorted_problem_space)) == False

def test_binary_search_iterative_contains_target_left_side():
    assert binary_search_iterative(problem_space, 5) == True


def test_binary_search_iterative__contains_target_midpoint():
    assert binary_search_iterative(problem_space, 303) == True


def test_binary_search_iterative__contains_right_side():
    assert binary_search_iterative(problem_space, 2000) == True


def test_binary_search_iterative__not_contains_target():
    assert binary_search_iterative(problem_space, 100) == False


def test_binary_search_iterative__empty_input():
    assert binary_search_iterative([], 1) == False