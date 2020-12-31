# -*- coding: UTF-8 -*-

# 入力
n = int(input())
for i in range(2**n):
    # '0b'は無視して2進数へ変換
    bin_i = str(bin(i))[2:]
    # 前半部出力
    print(str(i) + ':', end='')
    for idx, j in enumerate(reversed(bin_i)):
        # bitが立っているとき
        if j == '1':
            # 後半部出力
            print(' ' + str(idx), end='')
    # 改行
    print()