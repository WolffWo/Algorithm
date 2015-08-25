#! /usr/bin/env python
import timeit, math

"""
Sieve of Eratosthenes better version

When the algorithm terminates,
the numbers remaining in the array are
all the primes below n.

autor: wolffwo
"""


def sieve(n):
    arr = []  # create array
    for i in range(2, n):
        arr.append(i)  # fill array with all number between 2 and N
    for k in range(2, int(math.sqrt(n)+1)):
        if k in arr:
            for j in range(k, int(n/k)+1):
                if k*j in arr:
                    arr.remove(k*j)  # remove number
    return arr  # array with all prime numbers

prime = []
result = [[]]*3
for n in range(1, 4):
    print 'calc run-time for :' + str(pow(10, n))  # print lenght of array
    start = timeit.default_timer()  # start measure time
    prime = sieve(pow(10, n))  # calc prime numbers
    stop = timeit.default_timer()  # stop measure time
    time = stop - start  # print run-time
    result[n-1] = [pow(10, n), time, len(prime)]

print "| n    | time  | # prime numbers  |"
print "|------|-------|------------------|"
for n in range(1, 4):
    print "| " + str(result[n-1][0]) + " | " + str(result[n-1][1]) + " |",
    print str(result[n-1][2]) + " |"
print sieve(100)
