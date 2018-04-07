# https://www.hackerrank.com/challenges/maximize-it/problem

#   Sorted List Approach

# Functions


def get_val(selIdx, arr):
    valArr = []
    for i in range(len(arr)):
        valArr.append(arr[i][int(selIdx[i])])
    return valArr


def get_mod(selIdx, arr):
    sum = 0
    for i in range(len(arr)):
        sum += (arr[i][int(selIdx[i])])
    return sum%M

# Main Code
#   Obtain Lists
(K, M) = [int(ele) for ele in (input().split(' '))]

Ni = []
listArr = []
selIdx = []
modArr = []
sortModArr = []
for i in range(K):
    lst = input().strip().split(' ')
    sqlst = [int(e)*int(e) for e in lst]
    sqlst.sort()
    listArr.append(sqlst)
    mlst = [int(e)%M for e in sqlst]
    modArr.append(sorted(mlst))

#   Start of Processing

selIdx = [len(ar) - 1 for ar in modArr]
print(get_val(selIdx, modArr))
print(get_mod(selIdx, modArr))