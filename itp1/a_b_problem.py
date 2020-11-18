# -*- coding: UTF-8 -*-

# 入力
a, b = map(int, input().split())
# 出力
print(a//b, a%b, '{:.05f}'.format(a/b))