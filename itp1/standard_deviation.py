# -*- coding: UTF-8 -*-

for _ in range(10**9+7):
    # 入力
    n = int(input())
    if n == 0:
        break
    s = list(map(int, input().split()))
    # 平均値
    m = sum(s) / n
    # 分散
    a2 = 0
    for i in s:
        a2 += (i - m) ** 2
    a2 /= n
    # 標準偏差
    a = a2 ** 0.5
    # 出力
    print(a)