# -*- coding: UTF-8 -*-

# 入力
n, m, l = map(int, input().split())
A = [None] * n
for i in range(n):
    A[i] = list(map(int, input().split()))
B = [None] * m
for i in range(m):
    B[i] = list(map(int, input().split()))
C = [[0 for _ in range(l)] for __ in range(n)]
# 計算
for i in range(n):
    for j in range(l):
        for k in range(m):
            C[i][j] += A[i][k] * B[k][j]
# 出力
for i in C:
    print(*i)