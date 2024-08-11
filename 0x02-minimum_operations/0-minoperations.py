#!/usr/bin/python3
""" Module for 0-minoperations"""


def minOperations(n):
    """
    minOperations
    Gets fewest # of operations needed to result in exactly n H characters
    """

    if (n < 2):
        return 0
    operations = 0;
    divisor = 2;
    while divisor <= n:
        # if n evenly divides by root
        if n % divisor == 0:
            # total even-divisions by root = total operations
            operations += divisor
            # set n to the remainder
            n = n / divisor
            # reduce divisor to find remaining smaller vals that evenly-divide n
            divisor -= 1
        # increment divisor until it evenly-divides n
        divisor += 1
    return operations
