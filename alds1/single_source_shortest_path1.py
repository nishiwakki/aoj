# -*- coding: UTF-8 -*-

INF = 10**12
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
# 最短経路木
T = []
for _ in range(INF):
    u = None
    minv = INF
    for v in range(n):
        if v in T:
            continue
        if dist[v] < minv:
            u = v
            minv = dist[v]
    if u == None:
        break
    T.append(u)
    while adj[u]:
        v, weight = adj[u].pop()
        if v in T:
            continue
        if dist[v] > dist[u] + weight:
            dist[v] = dist[u] + weight
# 出力
for v, dv in enumerate(dist):
    print(v, dv)