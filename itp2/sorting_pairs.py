# -*- coding: UTF-8 -*-

# 入力
n = int(input())
xy = []
for i in range(n):
    x, y = map(int, input().split())
    xy.append([x, y])
# yで昇順ソート
xy.sort(key=lambda x: x[1])
# xで昇順ソート
xy.sort(key=lambda x: x[0])
# 出力
for i in iter(xy):
    print(i[0], i[1])