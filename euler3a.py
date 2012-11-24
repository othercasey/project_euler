from math import sqrt

number = 8462696833

ohai = sqrt(number)
ohai = int(ohai)

def prime(factor):
    squid = sqrt(factor) + 1
    squid = int(squid)
    for x in range(2, squid):
        if factor % x == 0:
            return False
    return True

list_of_awesometasticness = []

for x in range(1, number):
    if number % x == 0:
        print number / x
        if prime(number / x):
            print "Casey, pick " + str(number / x)
            break