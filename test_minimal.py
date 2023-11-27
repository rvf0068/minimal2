"""Tests for the minimal package"""

from minimal import my_sum


def test_sum():
    assert my_sum(2, 3) == 5
