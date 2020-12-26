# -*- coding: UTF-8 -*-

# 二分探索
def binarySearch(A, key):
    left = 0
    right = len(A)
    while left < right:
        mid = (left + right) // 2
        if A[mid] == key:
            return mid
        elif key < A[mid]:
            right = mid
        else:
            left = mid + 1
    return -1

# 入力
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
for bb in b:
    if binarySearch(a, bb) == -1:
        print(0)
        exit()
print(1)