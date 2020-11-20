# -*- coding: UTF-8 -*-

for _ in range(10**9+7):
    # 入力
    x = input()
    # EOF
    if x == '0':
        break
    ans = sum([int(i) for i in x])
    # 出力
    print(ans)