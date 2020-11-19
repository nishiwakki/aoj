# -*- coding: UTF-8 -*-

for _ in range(1000):
    # 入力
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    # フレーム作成
    frame1 = ''.join(['#' if i % 2 == 0 else '.' for i in range(W)])
    frame2 = ''.join(['.' if i % 2 == 0 else '#' for i in range(W)])
    # 出力
    for h in range(H):
        if h % 2 == 0:
            print(frame1)
        else:
            print(frame2)
    print()