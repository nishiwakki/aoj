# -*- coding: UTF-8 -*-

# 優先度付きキューlibrary
import heapq

# 入力
n, q = map(int, input().split())
# n個分のリスト用意
queue = [[] for _ in range(n)]
# リストを優先度付きキューに変換
for que in queue:
    heapq.heapify(que)
for _ in range(q):
    # クエリ入力
    query = list(map(int, input().split()))
    # insert(t, x)
    if query[0] == 0:
        heapq.heappush(queue[query[1]], -query[2])
    # getMax(t)
    elif query[0] == 1:
        if len(queue[query[1]]) > 0:
            p = -heapq.heappop(queue[query[1]])
            print(p)
            heapq.heappush(queue[query[1]], -p)
    # deleteMax(t)
    else:
        if len(queue[query[1]]) > 0:
            heapq.heappop(queue[query[1]])