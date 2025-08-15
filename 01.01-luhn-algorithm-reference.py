"""
Luhn algorithm is a simple verification scheme used for instance for credit card numbers.

The algorithm uses a check digit - typically the last digit in the number sequence - to verify
that the entire number is valid.

The check digit is calculated from all the preceding digits
using the Luhn formula. When validating a number, the algorithm recalculates what the check
digit should be and compares it to the actual last digit. If they match, the number is valid.

A possible interface could be something like verify(digits) where digits is a string of decimal digits, and verify just returns true or false. Once you have a working solution, tidy and/or refactor it until you're happy with it. I'll use this as an excuse to introduce some of the ideas and techniques we'll dive deeper into during this course.

- Double every second digit from the rightmost digit:

Starting from the rightmost digit of the number and moving left, double the value of every second digit.

- Handle doubled digits greater than 9:

If doubling a digit results in a two-digit number (i.e., greater than 9), subtract 9 from that doubled value to get a single digit. For example, if 6 is doubled to 12, subtract 9 to get 3.

- Sum all digits:

Add together all the digits, including the unmodified digits from the original number and the results from step 2.

- Check for divisibility by 10:

If the total sum is divisible by 10 (i.e., the sum modulo 10 equals 0), the number is considered valid according to the Luhn algorithm; otherwise, it is invalid.

The Luhn algorithm is designed to protect against accidental data entry errors, such as single-digit errors or transpositions of adjacent digits, but it is not intended to be a robust security measure against malicious attacks.
"""

LOOKUPS = (
    dict(zip("0123456789", (0, 1, 2, 3, 4, 5, 6, 7, 8, 9))),
    dict(zip("0123456789", (0, 2, 4, 6, 8, 1, 3, 5, 7, 9))),
)


def verify(digits):
    return (
        sum(LOOKUPS[i % 2][d] for i, d in enumerate(reversed(digits)))
        % 10
        == 0
    )


def test_luhn_algorithm():
    test_cases = [
        # (input, expected, description)
        ("4532015112830366", True, "Valid credit card number"),
        ("6011514433546201", True, "Valid credit card number"),
        ("378282246310005", True, "Valid American Express number"),
        ("5555555555554444", True, "Valid MasterCard test number"),
        ("4111111111111111", True, "Valid Visa test number"),
        ("79927398713", True, "Valid 11-digit number"),
        (
            "4532015112830367",
            False,
            "Last digit changed (invalid checksum)",
        ),
        ("1234567890123456", False, "Sequential digits (invalid)"),
        ("0000000000000000", True, "All zeros"),
        ("4532015112830365", False, "Off by 1 from valid number"),
        ("79927398712", False, "Off by 1 from valid number"),
        ("0", True, "Single digit (valid - checksum is 0)"),
        ("18", True, "Two digits (valid)"),
        ("17", False, "Two digits (invalid)"),
    ]

    for digits, expected, description in test_cases:
        result = verify(digits)
        assert result == expected, (
            f"{description}: verify('{digits}') returned {result}, expected {expected}"
        )

    print("All test cases passed!")


test_luhn_algorithm()
