import math as m
import pytest  
from equl import equalize


def test_pos_int_diff():
    assert equalize(1, 2) == 5.1962

def test_negativ_nambers():
    assert equalize(2, -1) == 0.3333

def test_zero():
    with pytest.raises(ZeroDivisionError) as er:
        assert equalize(2, 2) in str(er.value)

def test_pos_namber():
    assert equalize(0.2, 0.1) == 1.6432

def test_negetive_root():
    assert equalize(1, -2) == "dsjh"

def test_error_input():
    assert equalize("cush", 0) == "cush"
    assert equalize("", 0) == "cush"
    assert equalize("10 ** -9", 0) == "cush"