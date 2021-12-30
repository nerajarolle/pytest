import math

import pytest

products = [
   (2, 3, 6),  # two integers
   (1, 99, 99),
   (0, 99, 0),
   (5, -2, -10)

]


# def test_sqrt():
#     num = 25
#     assert math.sqrt(num) == 5
#
#
# def testsquare():
#     num = 7
#     assert 7 * 7 == 4
#
#
# def tesequality():
#    assert 10 == 11


@pytest.mark.parametrize('a, b, product', products)
def test_multiply(a, b, product):
    assert a * b == product
