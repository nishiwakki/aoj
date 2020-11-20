# -*- coding: UTF-8 -*-

for _ in range(10**9):
    # 入力
    n, x = map(int, input().split())
    # EOF
    if n == 0 and x == 0:
        break
    # 出力する答えをカウントアップ
    ans = 0
    for i in range(1, n-1):
        for j in range(i+1, n):
            for k in range(j+1, n+1):
                if i + j + k == x:
                    ans += 1
    # 出力
    print(ans)