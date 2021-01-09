# -*- coding: UTF-8 -*-

import math

# 小数8桁まで表示する関数
def pprint(x, y):
    print('{:.8f}'.format(x), '{:.8f}'.format(y))

# 2点p1,p2のs,u,tを計算する関数
def koch(p1x, p1y, p2x, p2y):
    sx = p1x + (p2x - p1x) / 3
    sy = p1y + (p2y - p1y) / 3
    tx = p2x - (p2x - p1x) / 3
    ty = p2y - (p2y - p1y) / 3
    ux = sx + \
         (tx - sx) * math.cos(math.radians(60)) - \
         (ty - sy) * math.sin(math.radians(60))
    uy = sy + \
         (tx - sx) * math.sin(math.radians(60)) + \
         (ty - sy) * math.cos(math.radians(60))
    return p1x, p1y, sx, sy, ux, uy, tx, ty, p2x, p2y

# 再帰的に座標を計算して表示する関数
def kochCurve(rest, stx, sty, enx, eny):
    p1x, p1y, sx, sy, ux, uy, tx, ty, p2x, p2y \
        = koch(stx, sty, enx, eny)
    if rest:
        kochCurve(rest-1, p1x, p1y, sx, sy)
        kochCurve(rest-1, sx, sy, ux, uy)
        kochCurve(rest-1, ux, uy, tx, ty)
        kochCurve(rest-1, tx, ty, p2x, p2y)
    else:
        pprint(sx, sy)
        pprint(ux, uy)
        pprint(tx, ty)
        pprint(p2x, p2y)

n = int(input())
# 始点
pprint(0, 0)
# n=0だけ別処理
if n == 0:
    pprint(100, 0)
else:
    kochCurve(n-1, 0, 0, 100, 0)