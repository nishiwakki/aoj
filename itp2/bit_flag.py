# -*- coding: UTF-8 -*-

# 入力
q = int(input())
# ビット列
bit = 0
# クエリ処理
for _ in range(q):
    query = list(map(int, input().split()))
    if len(query) == 1:
        com = query[0]
    else:
        com, i = query[0], query[1]
    # 右からに修正
    # test(i)
    if com == 0:
        print((bit & (1 << i)) >> i)
    # set(i)
    elif com == 1:
        bit |= 1 << i
    # clear(i)
    elif com == 2:
        bit &= ~(1 << i)
    # flip(i)
    elif com == 3:
        bit ^= 1 << i
    # all
    elif com == 4:
        if bit == 2**64 - 1:
            print(1)
        else:
            print(0)
    # any
    elif com == 5:
        if not bit == 0:
            print(1)
        else:
            print(0)
    # none
    elif com == 6:
        if bit == 0:
            print(1)
        else:
            print(0)
    # count
    elif com == 7:
        print(str(bin(bit)).count('1'))
    # val
    else:
        print(bit)