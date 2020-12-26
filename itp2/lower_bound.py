# -*- coding: UTF-8 -*-

# 配列二部法アルゴリズム
import bisect

# 入力
n = int(input())
a = list(map(int, input().split()))
q = int(input())
for i in range(q):
    k = int(input())
    # kをaのどの位置にいれるかをサーチ
    print(bisect.bisect_left(a, k))