# -*- coding: UTF-8 -*-

# 再帰呼び出し上限
import sys
sys.setrecursionlimit(10**4)

# メモ化再帰
memo = [-1] * 50
def fib(n):
    if memo[n] == -1:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

# 入力
n = int(input())
memo[0], memo[1] = 1, 1
# 出力
print(fib(n))