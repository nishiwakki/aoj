# -*- coding: UTF-8 -*-

# 入力
q = int(input())
# 辞書M
M = dict()
# query処理
for i in range(q):
    com = list(map(str, input().split()))
    # insert(key, x)
    if com[0] == '0':
        M[com[1]] = int(com[2])
    # get(key)
    else:
        print(M[com[1]])