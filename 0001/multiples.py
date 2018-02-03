#!/usr/bin/env python3
sum = 0
for number in range(1, 1000):
    if (not number % 3) or (not number % 5):
        # print(number)
        sum += number

print(sum)
