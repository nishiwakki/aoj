# -*- coding: UTF-8 -*-

# 出力
for i in range(10**9+7):
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    print(min(x, y), max(x, y))