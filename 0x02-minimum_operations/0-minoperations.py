#!/usr/bin/python3
""" Module for 0-minoperations"""
def minOperations(n):

"""
minOperations
Gets fewest # of operations needed to result in exactly n H characters
"""
if n <= 1:
return 0
divisor = 2
operations = 0
while n > 1:
# if n evenly divides by root
if n % divisor == 0
n = n / divisor
operations = operations + divisor
else:
divisor += 1
return operations
