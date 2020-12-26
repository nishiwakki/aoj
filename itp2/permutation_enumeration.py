# -*- coding: UTF-8 -*-

from itertools import permutations

# 入力
n = int(input())
# 順列全列挙
for pat in list(permutations(range(1, n+1))):
    print(*pat)