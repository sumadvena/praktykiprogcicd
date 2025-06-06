import pytest
from conversion import decimal_to_binary


@pytest.mark.parametrize(
    "decimal, expected_binary",
    [
        (0, "0"),
        (1, "1"),
        (2, "10"),
        (5, "101"),
        (10, "1010"),
        (16, "10000"),
        (31, "11111"),
        (64, "1000000"),
        (100, "1100100"),
    ],
)
def test_valid_inputs(decimal, expected_binary):
    """Test known conversions from decimal to binary."""
    assert decimal_to_binary(decimal) == expected_binary


def test_edge_cases():
    """Test the lower and upper bounds explicitly."""
    assert decimal_to_binary(0) == "0"
    assert decimal_to_binary(100) == "1100100"


@pytest.mark.parametrize(
    "invalid_input",
    [
        -1,  # below range
        101,  # above range
        3.14,  # not an integer
        "10",  # wrong type
        None,  # wrong type
        [],  # wrong type
        {},  # wrong type
    ],
)
def test_invalid_inputs_raise(invalid_input):
    """
    For inputs outside 0–100 or wrong types, the function should
    raise TypeError for non-integers, ValueError for out-of-range ints.
    """
    if isinstance(invalid_input, int):
        with pytest.raises(ValueError):
            decimal_to_binary(invalid_input)
    else:
        with pytest.raises(TypeError):
            decimal_to_binary(invalid_input)
