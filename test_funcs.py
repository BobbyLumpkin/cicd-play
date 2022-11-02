"""
Purpose: Some unit tests for funcs.py
"""


import pytest
from funcs import func1


@pytest.mark.unittest
def test_func1():
  assert func1() == "Hello, World!"
