# -*- coding: UTF-8 -*-

INFTY = 10 ** 10

def merge(A, left, mid, right):
    cnt = 0
    L = A[left:mid] + [INFTY]
    R = A[mid:right] + [INFTY]
    i, j = 0, 0
    for k in range(left, right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        cnt += 1
    return cnt

def mergeSort(A, left, right):
    cnt = 0
    if left+1 < right:
        mid = (left+right) // 2
        cnt += mergeSort(A, left, mid)
        cnt += mergeSort(A, mid, right)
        cnt += merge(A, left, mid, right)
    return cnt

# 入力
n = int(input())
S = list(map(int, input().split()))
# マージソート
cnt = mergeSort(S, 0, n)
# 出力
print(*S)
print(cnt)