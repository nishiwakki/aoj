# -*- coding: UTF-8 -*-

# 入力
x = int(input())
# 2進数表記
print('{:032b}'.format(x))
xx = ~x & (2 ** 32 - 1)
print('{:032b}'.format(xx))
# 左シフト
xx = x << 1
xx = str('{:032b}'.format(xx))
# 33桁になった時を考慮
if len(xx) == 32:
    print(xx)
else:
    print(xx[1:])
# 右シフト
xx = x >> 1
print('{:032b}'.format(xx))