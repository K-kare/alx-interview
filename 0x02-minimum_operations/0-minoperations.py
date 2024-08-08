<<<<<<< HEAD
#!/usr/bin/python3

def minOperations(n):
    """
    minOperations
    Gets fewest # of operations needed to result in exactly n H characters
    """
    if n <= 1:
        return 0
    
    operations = 0
    divisor = 0

    while n > 1:
        # if n evenly divides by root
        if n % divisor == 0:
            # total even-divisions by root = total operations
            n = n / divisor
            operations = operations + divisor

        else:
             # increment root until it evenly-divides n
            divisor += 1
    return operations
=======
#!/usr/bin/python3

def minOperations(n):
    """
    minOperations
    Gets fewest # of operations needed to result in exactly n H characters
    """
    if n <= 1:
        return 0
    
    operations = 0
    divisor = 0

    while n > 1:
        # if n evenly divides by root
        if n % divisor == 0:
            # total even-divisions by root = total operations
            n = n / divisor
            operations = operations + divisor

        else:
             # increment root until it evenly-divides n
            divisor += 1
    return operations
>>>>>>> f6299c2771438d50487f54afcd0e73a55b80897b
