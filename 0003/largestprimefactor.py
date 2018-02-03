#!/usr/bin/env python3
import math
import sys


def isPrime(number):
    """Returns True if n is prime.
        https://stackoverflow.com/a/1801446
    """
    if number == 2:
        return True
    if number == 3:
        return True
    if number % 2 == 0:
        return False
    if number % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= number:
        if number % i == 0:
            return False

        i += w
        w = 6 - w

    return True


def primeGenerator(stop):
    yield 2
    number = 3
    while number <= stop:
        if isPrime(number):
            print(
                    "curent PrimeNumber: {}".format(
                            number
                        )
                    )
            yield number
        number += 2


def getPrimeFactors(number):
    factors = []
    for prime in primeGenerator(int(math.ceil(math.sqrt(number)))):
        if number % prime == 0:
            factors.append(prime)
    return factors


input = 600851475143
# for the love of god dont do this
# input = sys.maxsize
print(getPrimeFactors(input))


# old one dont use!
def primeGeneratorOld(stop):
    number = 3
    primes = [2]
    while True:
        isPrime = True
        for i in range(primes[0], number):
            if number % i == 0:
                isPrime = False
                continue
        else:
            if isPrime:
                print(
                    "primes size: {} curent PrimeNumber: {}".format(
                            len(primes) + 1,
                            number
                        )
                    )
                yield number
                primes.append(number)
            if number == stop:
                return
            number += 2


# Memmory hog likea mofo!
# will kill the comp
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


def getPrimeFactorsOld(number):
    factors = []
    primeNumbers = getPrimeNumbers(2, number)
    for prime in primeNumbers:
        if number % prime == 0:
            factors.append(prime)
    return factors
