# test_my_math.py

import pytest
from my_math import add

def test_add():
    assert add(2, 3) == 5
    assert add(1, 1) == 2
    assert add(1, 1) == 2

def test_add_with_strings():
    with pytest.raises(TypeError):
        add('2', 3)
