def isPalindrome(num):
    return str(num) == str(num)[::-1]


# I'm an idiot this aint working
# because it doesnt go throught all the possible
# combination
def getHighestPalindrome1(x, y):
    z = 0
    while True:
        if x >= 999 and y <= 100:
            print(x)
            print(y)
            break
        temp = x*y
        if isPalindrome(temp):
            if temp > z:
                z = temp
        x += 1
        temp = x*y
        if isPalindrome(temp):
            if temp > z:
                z = temp
        y -= 1
        temp = x*y
        if isPalindrome(temp):
            if temp > z:
                z = temp
    return z


def getHighestPalindrome2(bot, top):
    z = 0
    for x in range(bot, top, 1):
        for y in range(bot, top, 1):
            if isPalindrome(x*y):
                if x*y >= z:
                    z = x*y
    return z


print(getHighestPalindrome1(100, 999))
print(getHighestPalindrome2(100, 999))
