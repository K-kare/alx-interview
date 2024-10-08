#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Method that determines if a given data set represents a valid
    UTF-8 encoding.
    """
    number_bytes = 0

    mask_a = 1 << 7
    mask_b = 1 << 6

    for digit in data:

        mask_byte = 1 << 7

        if number_bytes == 0:

            while mask_byte & digit:
                number_bytes += 1
                mask_byte = mask_byte >> 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            if not (digit & mask_a and not (digit & mask_b)):
                    return False

        number_bytes -= 1

    if number_bytes == 0:
        return True

    return False
