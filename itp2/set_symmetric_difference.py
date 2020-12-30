# -*- coding: UTF-8 -*-

# 入力
n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))
# aとbの対象差集合、昇順ソート
ab = sorted(list(a ^ b))
# 出力
for i in ab:
    print(i)