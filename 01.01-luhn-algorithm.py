"""
Luhn algorithm is a simple verification scheme used for instance for credit card numbers.

A possible interface could be something like verify(digits) where digits is a string of decimal digits, and verify just returns true or false. Once you have a working solution, tidy and/or refactor it until you're happy with it. I'll use this as an excuse to introduce some of the ideas and techniques we'll dive deeper into during this course.
"""


def verify(digits):
    pass


def test_luhn_algorithm():
    # Valid numbers (should return True)
    assert (
        verify("4532015112830366") == True
    )  # Valid credit card number
    assert (
        verify("6011514433546201") == True
    )  # Valid credit card number
    assert (
        verify("378282246310005") == True
    )  # Valid American Express number
    assert (
        verify("5555555555554444") == True
    )  # Valid MasterCard test number
    assert verify("4111111111111111") == True  # Valid Visa test number
    assert verify("79927398713") == True  # Valid 11-digit number

    # Invalid numbers (should return False)
    assert (
        verify("4532015112830367") == False
    )  # Last digit changed (invalid checksum)
    assert (
        verify("1234567890123456") == False
    )  # Sequential digits (invalid)
    assert verify("0000000000000000") == False  # All zeros (invalid)
    assert (
        verify("4532015112830365") == False
    )  # Off by 1 from valid number
    assert verify("79927398712") == False  # Off by 1 from valid number

    # Edge cases
    assert verify("0") == True  # Single digit (valid - checksum is 0)
    assert verify("18") == True  # Two digits (valid)
    assert verify("17") == False  # Two digits (invalid)

    print("All test cases passed!")


if __name__ == "__main__":
    test_luhn_algorithm()
