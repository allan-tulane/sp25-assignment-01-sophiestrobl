"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.


def foo(x):
    if x <= 1:
        return x
    else:
        ra = foo(x - 1)
        rb = foo(x - 2)
        return ra + rb


def longest_run(myarray, key):
    max_run = 0
    current_run = 0

    for num in myarray:
        if num == key:
            current_run += 1
            max_run = max(max_run, current_run)
        else:
            current_run = 0  # Reset count when encountering a different number

    return max_run


class Result:
    """ done """

    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size  # run on left side of input
        self.right_size = right_size  # run on right side of input
        self.longest_size = longest_size  # longest run in input
        self.is_entire_range = is_entire_range  # True if the entire input matches the key

    def __repr__(self):
        return (
            'longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
            (self.longest_size, self.left_size, self.right_size,
             self.is_entire_range))


def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)


def longest_run_recursive(mylist, key):
    # Base case if the list is empty
    if len(mylist) == 0:
        return Result(0, 0, 0, False)

    # Base case if there's only one element
    if len(mylist) == 1:
        is_match = mylist[0] == key
        return Result(int(is_match), int(is_match), int(is_match), is_match)

    # split list into two halves
    mid = len(mylist) // 2
    left_result = longest_run_recursive(mylist[:mid], key)
    right_result = longest_run_recursive(mylist[mid:], key)

    # Merge left and right results and check if the entire range is the key
    is_entire_range = left_result.is_entire_range and right_result.is_entire_range

    # Compute left_size
    left_size = left_result.left_size if not left_result.is_entire_range else left_result.left_size + right_result.left_size

    # Compute right_size
    right_size = right_result.right_size if not right_result.is_entire_range else right_result.right_size + left_result.right_size

    # Compute the longest_size
    spanning_size = left_result.right_size + right_result.left_size
    longest_size = max(left_result.longest_size, right_result.longest_size,
                       spanning_size)

    return Result(left_size, right_size, longest_size, is_entire_range)
