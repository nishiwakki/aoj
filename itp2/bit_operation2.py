# -*- coding: UTF-8 -*-

# 入力
a, b = map(int, input().split())
# AND
print('{:032b}'.format(a & b))
# OR
print('{:032b}'.format(a | b))
# XOR
print('{:032b}'.format(a ^ b))