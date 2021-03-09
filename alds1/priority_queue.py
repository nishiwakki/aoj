# -*- coding: UTF-8 -*-

import heapq
import sys
input = sys.stdin.readline

# 命令数上限
MAX_OP = 2 * 10 ** 6 + 2
ans = []
# 優先度付きキュー
pq = []
heapq.heapify(pq)
for _ in range(MAX_OP):
    query = list(map(str, input().split()))
    # insert(S, K)
    if len(query) == 2:
        heapq.heappush(pq, -int(query[1]))
    else:
        # extractMax(S)
        if query[0] == 'extract':
            ans.append(-heapq.heappop(pq))
        # end
        else:
            break
# 出力
for a in ans:
    print(a)