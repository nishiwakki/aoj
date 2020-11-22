# -*- coding: UTF-8 -*-

# 入力
x1, y1, x2, y2 = map(float, input().split())
ans = ((x2-x1)**2 + (y2-y1)**2) ** 0.5
# 出力
print(ans)