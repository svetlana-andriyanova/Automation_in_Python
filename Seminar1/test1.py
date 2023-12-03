import pytest
from task1 import check

def test_word(good_word, bad_word):
    assert good_word in check(bad_word)

if __name__ == "__main__":
    pytest.main(['-vv'])