# -*- coding: UTF-8 -*-

for _ in range(1000):
    # 入力
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    # 出力
    for h in range(H):
        for w in range(W):
            print('#', end='')
        print()
    print()