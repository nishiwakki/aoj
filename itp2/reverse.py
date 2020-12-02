# -*- coding: UTF-8 -*-

# 入力
n = int(input())
a = list(map(int, input().split()))
q = int(input())
for _ in range(q):
    b, e = map(int, input().split())
    a = a[:b] + list(reversed(a[b:e])) + a[e:]
# 出力
print(*a)