# -*- coding: UTF-8 -*-

# 可変長配列A
A = []
# 出力配列ans
ans = []
# 入力
q = int(input())
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        # pushBack(x): Aの末尾に整数xを挿入する
        A.append(query[1])
    elif query[0] == 1:
        # randomAccess(p): Aの要素apの値を出力する
        ans.append(A[query[1]])
    else:
        # popBack(): Aの末尾の要素を削除する
        A.pop(-1)
# ansを出力
for i in ans:
    print(i)