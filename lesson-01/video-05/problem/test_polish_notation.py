import pytest

from polish_notation import polish_notation
from polish_notation import reverse_polish_notation

def test_polish_notation_addition():
    assert polish_notation("3 4 +") == 7

def test_polish_notation_subtraction():
    assert polish_notation("10 4 -") == 6

def test_polish_notation_multiplication():
    assert polish_notation("3 4 *") == 12

def test_polish_notation_division():
    assert polish_notation("12 4 /") == 3

def test_polish_notation_complex_expression():
    assert polish_notation("5 1 2 + 4 * + 3 -") == 14

def test_polish_notation_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        polish_notation("4 0 /")

def test_reverse_polish_notation_addition():
    assert reverse_polish_notation("+ 3 4") == 7

def test_reverse_polish_notation_subtraction():
    assert reverse_polish_notation("- 10 4") == 6

def test_reverse_polish_notation_multiplication():
    assert reverse_polish_notation("* 3 4") == 12

def test_reverse_polish_notation_division():
    assert reverse_polish_notation("/ 12 4") == 3

def test_reverse_polish_notation_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        reverse_polish_notation("/ 4 0")
        
if __name__ == "__main__":
    pytest.main()