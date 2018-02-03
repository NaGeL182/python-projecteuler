#!/usr/bin/env python3


def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a+b


def iseven(number):
    return number % 2 == 0


sum = 0
for number in fibonacci():
    if number >= 4000000:
        break
    if not iseven(number):
        continue
    sum += number

print(sum)
