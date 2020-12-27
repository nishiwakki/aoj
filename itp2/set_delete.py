# -*- coding: UTF-8 -*-

# 入力
q = int(input())
# 集合S
S = set([])
# クエリ処理
for i in range(q):
    com, x = map(int, input().split())
    # insert(x)
    if com == 0:
        S.add(x)
        print(len(S))
    # find(x)
    elif com == 1:
        if x in S:
            print(1)
        else:
            print(0)
    # delete(x)
    else:
        if x in S:
            S.remove(x)