# -*- coding: UTF-8 -*-

# 個数を数えるライブラリ
from collections import Counter

# 入力
n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

C = Counter(S)
ans = 0
for t in T:
    # Cのキーにあるとき
    if t in C:
        ans += 1
print(ans)