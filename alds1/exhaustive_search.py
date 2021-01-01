# -*- coding: UTF-8 -*-

from copy import deepcopy

# 入力
n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))
# 作成可能な数をセットで管理
ans = set()
for a in A:
    for i in deepcopy(ans):
        ans.add(i+a)
    ans.add(a)
for m in M:
    # ansに存在するなら
    if m in ans:
        print('yes')
    else:
        print('no')