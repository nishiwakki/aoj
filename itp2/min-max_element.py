# -*- coding: UTF-8 -*-

# 入力
n = int(input())
a = list(map(int, input().split()))
q = int(input())
for _ in range(q):
    com, b, e = map(int, input().split())
    # min(b, e)
    if com == 0:
        print(min(a[b:e]))
    # max(b, e)
    else:
        print(max(a[b:e]))