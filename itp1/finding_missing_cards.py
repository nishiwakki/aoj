# -*- coding: UTF-8 -*-

# カード情報
shcd = [0] * 52
# 入力
n = int(input())
for i in range(n):
    mark, rank = map(str, input().split())
    rank = int(rank) - 1
    if mark == 'H':
        rank += 13
    elif mark == 'C':
        rank += 13 * 2
    elif mark == 'D':
        rank += 13 * 3
    # 1のとき手元にある
    shcd[rank] = 1
# 出力
for i in range(52):
    # 手元にないか?
    if shcd[i] == 0:
        if i < 13 * 1:
            print('S', i+1)
        elif i < 13 * 2:
            print('H', i-13+1)
        elif i < 13 * 3:
            print('C', i-13*2+1)
        else:
            print('D', i-13*3+1)