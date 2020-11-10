# -*- coding: UTF-8 -*-

def my_gcd(p, q):
    # ユークリッドの互除法
    while q != 0:
        r = p % q
        p = q
        q = r
    return p

x, y = map(int, input().split())
print(my_gcd(x, y))