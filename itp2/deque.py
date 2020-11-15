# -*- coding: UTF-8 -*-

from collections import deque

# 可変長配列A
A = deque()
# 出力配列ans
ans = []
# 入力
q = int(input())
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        # push(d, x)
        if query[1] == 0:
            # 先頭にpush
            A.appendleft(query[2])
        else:
            # 末尾にpush
            A.append(query[2])
    elif query[0] == 1:
        # randomAccess(p)
        ans.append(A[query[1]])
    else:
        # pop(d)
        if query[1] == 0:
            # 先頭の要素を削除
            A.popleft()
        else:
            # 末尾の要素を削除
            A.pop()
# ansを出力
for i in ans:
    print(i)