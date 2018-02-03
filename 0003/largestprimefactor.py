#!/usr/bin/env python3
import math


def getPrimeNumbers(start, number):
    array = [True for x in range(number)]
    i = start
    while True:
        print(i)
        if i > math.sqrt(number):
            break
        if array[i]:
            j = i ** 2
            while True:
                if j >= number:
                    break
                array[j] = False
                j += i
        i += 1

    return [index for index, val in enumerate(array)
            if val and index not in [0, 1]]


def getPrimeFactors(number):
    factors = []
    primeNumbers = getPrimeNumbers(2, number)
    for prime in primeNumbers:
        if number % prime == 0:
            factors.append(prime)
    return factors


input = 50000000
print(getPrimeFactors(input))
