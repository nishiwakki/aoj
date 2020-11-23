# -*- coding: UTF-8 -*-

# 入力
n, q = map(int, input().split())
# n個分のスタック用意
stack = [[] for _ in range(n)]
for _ in range(q):
    # クエリ入力
    query = list(map(int, input().split()))
    # push(t, x)
    if query[0] == 0:
        stack[query[1]].append(query[2])
    # top(t)
    elif query[0] == 1:
        if len(stack[query[1]]) > 0:
            print(stack[query[1]][-1])
    # pop(t)
    else:
        if len(stack[query[1]]) > 0:
            stack[query[1]].pop()