"""Tests for the minimal package"""

from minimal import my_sum


def test_sum():
    """A test for the sum function"""
    assert my_sum(2, 3) == 5
