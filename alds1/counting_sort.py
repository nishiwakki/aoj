# -*- coding: UTF-8 -*-

from itertools import accumulate

# 計数ソート
def CountingSort(A, B, k):
    A = [0] + A
    n = len(A)
    # カウント配列
    C = [0] * (k+1)
    # C[i] に i の出現数を記録する
    for j in range(1, n):
        C[A[j]] += 1
    # C[i] に i 以下の数の出現数を記録する
    # 累積和を計算
    C = list(accumulate(C))
    for j in range(n, 0, -1):
        B[C[A[j-1]]] = A[j-1]
        C[A[j-1]] -= 1
    return B

# 入力
n = int(input())
A = list(map(int, input().split()))
# 計数ソート
B = CountingSort(A, [0]*(n+1), 10001)
# 出力
print(*B[1:])