# -*- coding: UTF-8 -*-

from itertools import permutations
from math import factorial

# 入力
n = int(input())
a = tuple(map(int, input().split()))
# n=1の場合
if n == 1:
    print(1)
    exit()
# 順列全列挙
pats = list(permutations(range(1, n+1)))
# 概要順列が何番目か
ans = 0
for idx, pat in enumerate(pats):
    # 一致する場合
    if pat == a:
        ans = idx
        break
# 先頭だったとき
if ans == 0:
    print(*pats[0])
    print(*pats[1])
# 最後だったとき
elif ans == factorial(n) - 1:
    print(*pats[ans-1])
    print(*pats[ans])
# それ以外
else:
    print(*pats[ans-1])
    print(*pats[ans])
    print(*pats[ans+1])