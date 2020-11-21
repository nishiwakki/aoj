# -*- coding: UTF-8 -*-

for _ in range(10**9+7):
    # 最初の並びを表す文字列入力
    s = input()
    if s == '-':
        break
    # シャッフル回数
    shuffle = 0
    # シャッフル回数入力
    m = int(input())
    for i in range(m):
        shuffle += int(input())
    # 1周で元どおり
    shuffle %= len(s)
    # 出力
    print(s[shuffle:] + s[:shuffle])