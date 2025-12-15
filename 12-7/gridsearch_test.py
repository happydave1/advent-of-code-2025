import pytest
from gridsearch import *

def test1():
    assert grid_search(3, 7) == 28

def test2():
    assert grid_search(3, 2) == 3

def test3():
    # testing runtime
    assert grid_search(23, 12) == 193536720