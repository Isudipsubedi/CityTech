import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from inversion_counter import count_inversions

def test_empty_array():
    assert count_inversions([]) == 0

def test_single_element():
    assert count_inversions([5]) == 0

def test_sorted_array():
    assert count_inversions([1, 2, 3, 4, 5]) == 0

def test_reverse_sorted():
    assert count_inversions([5, 4, 3, 2, 1]) == 10

def test_mixed_case():
    assert count_inversions([1, 20, 6, 4, 5]) == 5

def test_large_array():
    big_arr = list(range(1000, 0, -1))
    expected = (1000 * 999) // 2
    assert count_inversions(big_arr) == expected

"""
To run the tests, execute the following command:

pip install -r requirements.txt
python -m pytest tests/ -v

"""