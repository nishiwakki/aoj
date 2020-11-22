# -*- coding: UTF-8 -*-

import math

# 入力
a, b, C = map(int, input().split())
# Cを度数からラジアンへ変換
C = math.radians(C)
# sin(C)を求める
sinC = math.sin(C)
# cos(C)を求める
cosC = math.cos(C)
# 余弦定理でcを求める
c = (a**2 + b**2 - 2*a*b*cosC) ** 0.5
# 三角形の面積S
S = a * b * sinC / 2
# 底辺*高さ/2
h = S * 2 / a
# 周の長さ
L = a + b + c
# 出力
print(S)
print(L)
print(h)