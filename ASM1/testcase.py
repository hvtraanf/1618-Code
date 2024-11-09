from binarysearch import binary_search

import pytest

class TestBinarySearch:

    # Search for an element that exists in the middle of the array
    def test_search_element_in_middle(self):
        arr = [1, 2, 3, 4, 5]
        x = 3
        result = binary_search(arr, x)
        if result == 2:
            print("Test case 1 (element in middle): PASSED")
        else:
            print("Test case 1 (element in middle): FAILED")

    # Search in an empty array
    def test_search_in_empty_array(self):
        arr = []
        x = 3
        result = binary_search(arr, x)
        if result == -1:
            print("Test case 2 (empty array): PASSED")
        else:
            print("Test case 2 (empty array): FAILED")

    # Search for an element that exists at the beginning of the array
    def test_search_element_at_beginning(self):
        arr = [1, 2, 3, 4, 5]
        x = 1
        result = binary_search(arr, x)
        if result == 0:
            print("Test case 3 (element at beginning): PASSED")
        else:
            print("Test case 3 (element at beginning): FAILED")

    # Search for an element that exists at the end of the array
    def test_search_element_at_end(self):
        arr = [1, 2, 3, 4, 5]
        x = 5
        result = binary_search(arr, x)
        if result == 4:
            print("Test case 4 (element at end): PASSED")
        else:
            print("Test case 4 (element at end): FAILED")

# Running the tests
test = TestBinarySearch()
test.test_search_element_in_middle()
test.test_search_in_empty_array()
test.test_search_element_at_beginning()
test.test_search_element_at_end()
