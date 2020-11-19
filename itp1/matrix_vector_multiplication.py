# -*- coding: UTF-8 -*-

# 入力
n, m = map(int, input().split())
A = [None] * n
for i in range(n):
    A[i] = list(map(int, input().split()))
B = [0] * m
for i in range(m):
    B[i] = int(input())
# 計算, 出力
for i in range(n):
    ans = 0
    for j in range(m):
        ans += A[i][j] * B[j]
    print(ans)