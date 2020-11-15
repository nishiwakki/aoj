# -*- coding: UTF-8 -*-

# 入力
a, b = map(int, input().split())
# 面積
ans1 = a * b
# 周の長さ
ans2 = 2 * (a+b)
# 出力
print(ans1, ans2)