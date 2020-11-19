# -*- coding: UTF-8 -*-

# 入力
n = int(input())
a = list(map(int, input().split()))
a.reverse()
# 出力
print(*a)