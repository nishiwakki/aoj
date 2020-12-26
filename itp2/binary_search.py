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
q = int(input())
for i in range(q):
    k = int(input())
    # 二分探索
    # 見つからない場合
    if binarySearch(a, k) == -1:
        print(0)
    # 見つかった場合
    else:
        print(1)