# -*- coding: UTF-8 -*-

from collections import deque

# 入力
n, q = map(int, input().split())
# n個分のキュー用意
queue = [deque() for _ in range(n)]
for _ in range(q):
    # クエリ入力
    query = list(map(int, input().split()))
    # enqueue(t, x)
    if query[0] == 0:
        queue[query[1]].append(query[2])
    # front(t)
    elif query[0] == 1:
        if len(queue[query[1]]) > 0:
            print(queue[query[1]][0])
    # dequeue(t)
    else:
        if len(queue[query[1]]) > 0:
            queue[query[1]].popleft()