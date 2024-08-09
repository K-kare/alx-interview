#!/usr/bin/python3
""" Module for 0-minoperations"""

 def minOperations(n):
    """
    Calculate the minimum number of operations required to get exactly n 'H' characters
    in the file starting with one 'H', using only the 'Copy All' and 'Paste' operations.

    Parameters:
    n (int): The number of 'H' characters desired in the file.

    Returns:
    int: The minimum number of operations required to achieve exactly n 'H' characters.
         If n is impossible to achieve, return 0.
    """
    if (n < 2):
        return 0
    operations = 0
    divisor = 2 
    while n > 1:
        # if n evenly divides by root
        if n % divisor == 0:
            # total even-divisions by root = total operations
            n = n / divisor
            operations = operations + divisor
       else:
           divisor += 1
    return operations
