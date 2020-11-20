# -*- coding: UTF-8 -*-

# 入力
r, c = map(int, input().split())
# 表作成
mat = [None] * (r + 1)
# 入力適応
for i in range(r):
    mat[i] = list(map(int, input().split())) + [0]
mat[r] = [0] * (c+1)
# 行合計
for i in range(r):
    mat[i][c] = sum(mat[i][0:c])
# 列合計
for i in range(c+1):
    val = 0
    for j in range(r):
        val += mat[j][i]
    mat[r][i] = val
# 出力
for i in mat:
    print(*i)