# -*- coding: UTF-8 -*-

for _ in range(100000):
    # 入力
    a, op, b = map(str, input().split())
    a, b = int(a), int(b)
    # 出力
    if op == '?':
        break
    elif op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    elif op == '/':
        print(a // b)