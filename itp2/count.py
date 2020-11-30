# -*- coding: UTF-8 -*-

# 入力
n = int(input())
a = list(map(int, input().split()))
q = int(input())
for _ in range(q):
    b, e, k = map(int, input().split())
    # 出力
    print(a[b:e].count(k))