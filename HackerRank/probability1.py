# https://www.hackerrank.com/challenges/iterables-and-iterators/problem

from math import factorial


def C(n, r):
    return int(factorial(n) / factorial(r) / factorial(n - r))


N = int(input())
lst = list(input().split(' ')[:N])
K = int(input())

psets = C(N, K)         # Possible number of sets
match = 0

for ele in lst:
    if ele == 'a':
        match += 1

"""
If there are `p` possible sets, among which `m` elements shouldn't be present in the final combo, we get:
res = p - C(N-m, K)
"""

if N-match>=K>=0 :
    dset = C(N-match, K)    # Desired set
else: dset=0

print(1 - dset/psets)