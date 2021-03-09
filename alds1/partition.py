# -*- coding: UTF-8 -*-

def partition(L, p, r):
    x = L[r]
    i = p - 1
    for j in range(p, r):
        if L[j] <= x:
            i += 1
            L[i], L[j] = L[j], L[i]
    L[i+1], L[r] = L[r], L[i+1]
    return i+1

# 入力
n = int(input())
A = list(map(int, input().split()))
pi = partition(A, 0, n-1)
# 出力
for idx, a in enumerate(A):
    if idx == n-1:
        print(a)
    elif idx == pi:
        print('['+str(a)+']', end=' ')
    else:
        print(a, end=' ')