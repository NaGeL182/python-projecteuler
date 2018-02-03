#!/usr/bin/env python3
import math


def primeGenerator(stop):
    number = 2
    primes = [2]
    while True:
        isPrime = True
        for i in range(primes[0], number):
            if number % i == 0:
                isPrime = False
                continue
        else:
            if isPrime:
                yield number
                primes.append(number)
            if number == stop:
                return
            number += 1


def getPrimeFactors(number):
    factors = []
    for prime in primeGenerator(int(math.ceil(math.sqrt(number)))):
        print(prime)
        if number % prime == 0:
            factors.append(prime)
    return factors


input = 600851475143
print(getPrimeFactors(input))


# old one dont use!
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
