# https://www.hackerrank.com/challenges/maximize-it/problem

#   Brute Force Approach


def tuple_gen(n, K, lst, sel, combo):
    if(n==K-1):   # When we've reached the last list and all items for the tuple has been selected.
        for i in lst[n]:
            tup = tuple(sel) + (i,)
            combo.append(tup)
    else:
        for i in lst[n]:
            item = sel + list(i)
            tuple_gen(n+1, K, lst, item, combo)


# Main Code
(K, M) = [int(ele) for ele in (input().split(' '))]

Ni = []
listArr = []
for i in range(K):
    lst = input().strip().split(' ')[1:]
    listArr.append(lst)

combos = []
vals = []
tuple_gen(0, K, listArr, [], combos)

for tups in combos:
    sum = 0
    for el in tups:
        el = int(el)
        sum += (el*el)
    vals.append(sum%M)

print(max(vals))