# -*- coding: UTF-8 -*-

# 入力
n, q = map(int, input().split())
# 可変長配列A
A = [[] for _ in range(n)]
# 出力配列ans
ans = []
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        # pushBack(x): Atの末尾に整数xを挿入する
        A[query[1]].append(query[2])
    elif query[0] == 1:
        # dump(t): Atの全ての要素を出力する
        print(*A[query[1]])
    else:
        # clear(t): Atを空にする
        A[query[1]].clear()
# ansを出力
for i in ans:
    print(i)