# -*- coding: UTF-8 -*-

# 入力
W, H, x, y, r = map(int, input().split())
leftX, rightX = x - r, x + r
upY, downY = y + r, y - r
if not 0 <= leftX <= W:
    print('No')
elif not 0 <= rightX <= W:
    print('No')
elif not 0 <= upY <= H:
    print('No')
elif not 0 <= downY <= H:
    print('No')
else:
    print('Yes')