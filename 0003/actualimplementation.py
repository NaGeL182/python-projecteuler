#!/usr/bin/env python3
from timeit import default_timer as timer
import math
import sys

"""
Actual implementation acording to the overview pdf...
"""


def largestPrimeFactor1(number):
    orig = number
    start = timer()
    factor = 2
    lastFactor = 1
    while number > 1:
        if number % factor == 0:
            lastFactor = factor
            number = number / factor
            while number % factor == 0:
                number = number / factor
        factor += 1
    end = timer()
    return "{}'s largest factor is: {} time: {}".format(
            orig,
            lastFactor,
            end - start
        )


def largestPrimeFactor2(number):
    orig = number
    start = timer()
    if number % 2 == 0:
        number = number / 2
        lastFactor = 2
        while number % 2 == 0:
            number = number / 2
    else:
        lastFactor = 1
    factor = 3
    while number > 1:
        if number % factor == 0:
            number = number / factor
            lastFactor = factor
            while number % factor == 0:
                number = number / factor
        factor += 2
    end = timer()
    return "{}'s largest factor is: {} time: {}".format(
            orig,
            lastFactor,
            end - start
        )


def largestPrimeFactor3(number):
    orig = number
    start = timer()
    if number % 2 == 0:
        number = number / 2
        lastFactor = 2
        while number % 2 == 0:
            number = number / 2
    else:
        lastFactor = 1
    factor = 3
    maxFactor = math.sqrt(number)
    while number > 1 and factor <= maxFactor:
        if number % factor == 0:
            number = number / factor
            lastFactor = factor
            while number % factor == 0:
                number = number / factor
            maxFactor = math.sqrt(number)
        factor += 2
    end = timer()
    return "{}'s largest factor is: {} time: {}".format(
            orig,
            lastFactor if number == 1 else orig,
            end - start
        )


print(largestPrimeFactor1(13195))
print(largestPrimeFactor1(600851475143))
print(largestPrimeFactor1(sys.maxsize))
print(largestPrimeFactor2(13195))
print(largestPrimeFactor2(600851475143))
# bugs out number == 512 and factor >= 513 akesa lot of time
# till it reaches the number! Run it at your own risk
# print(largestPrimeFactor2(sys.maxsize))
print(largestPrimeFactor3(13195))
print(largestPrimeFactor3(600851475143))
print(largestPrimeFactor3(sys.maxsize))
