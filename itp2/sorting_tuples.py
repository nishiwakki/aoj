# -*- coding: UTF-8 -*-

# 入力
n = int(input())
items = []
for i in range(n):
    value, weight, type_, date, name = map(str, input().split())
    items.append([int(value), int(weight), type_, int(date), name])
# 優先度低い順からソート
items.sort(key=lambda x: x[4])
items.sort(key=lambda x: x[3])
items.sort(key=lambda x: x[2])
items.sort(key=lambda x: x[1])
items.sort(key=lambda x: x[0])
# 出力
for i in iter(items):
    print(*i)