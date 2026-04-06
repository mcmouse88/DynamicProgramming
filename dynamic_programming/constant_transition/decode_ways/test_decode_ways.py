import pytest
from dynamic_programming.constant_transition.decode_ways.decode_ways import (
    numDecodingsTopDown,
    numDecodingsBottomUp,
    numDecodings,
)

DECODE_CASES = [
    ("12", 2),
    ("226", 3),
    ("06", 0),
    ("11106", 2),
    ("10", 1),
    ("27", 1),
    ("1", 1),
    ("0", 0),
    ("100", 0),
    ("101", 1),
    ("111", 3),
    ("1111111111", 89),
    ("2611055971756562", 4),
]


@pytest.mark.parametrize("s, expected", DECODE_CASES)
def test_numDecodingsTopDown(s, expected):
    assert numDecodingsTopDown(s) == expected


@pytest.mark.parametrize("s, expected", DECODE_CASES)
def test_numDecodingsBottomUp(s, expected):
    assert numDecodingsBottomUp(s) == expected


@pytest.mark.parametrize("s, expected", DECODE_CASES)
def test_numDecodings(s, expected):
    assert numDecodings(s) == expected
