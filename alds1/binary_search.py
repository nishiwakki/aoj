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
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

ans = 0
for t in T:
    # 見つかった時カウントアップ
    if not binarySearch(S, t) == -1:
        ans += 1
print(ans)