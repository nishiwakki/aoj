# -*- coding: UTF-8 -*-

import heapq
import sys
input = sys.stdin.readline

INF = 10**9
# 入力
n = int(input())
# 隣接リスト作成
adj = [[] for _ in range(n)]
for i in range(n):
    info = list(map(int, input().split()))
    for j in range(1, info[1]+1):
        adj[info[0]].append([info[2*j], info[2*j+1]])
# 頂点0からの最短距離
dist = [INF] * n
# 始点0は距離0
dist[0] = 0
# 優先度付きキューで最短距離を管理
pq = [(dist[0], 0)]
heapq.heapify(pq)
# 最短既確定ノード
T = set()
while pq:
    cost, u = heapq.heappop(pq)
    if dist[u] < cost:
        continue
    T.add(u)
    while adj[u]:
        v, weight = adj[u].pop()
        if v in T:
            continue
        if dist[v] > dist[u] + weight:
            dist[v] = dist[u] + weight
            heapq.heappush(pq, (dist[v], v))
# 出力
for v, dv in enumerate(dist):
    print(v, dv)