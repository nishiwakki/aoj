# -*- coding: UTF-8 -*-

for _ in range(1000):
    # 入力
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    # フレーム作成
    frame1 = ''.join(['#' for _ in range(W)])
    frame2 = ''.join(['#'] + ['.' for _ in range(W-2)] + ['#'])
    # 出力
    print(frame1)
    for h in range(H-2):
        print(frame2)
    print(frame1)
    print()