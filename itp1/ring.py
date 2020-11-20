# -*- coding: UTF-8 -*-

# 入力
s = input()
p = input()
# sを2つ繋いで判定
s += s
# 出力
if s.count(p) >= 1:
    print('Yes')
else:
    print('No')