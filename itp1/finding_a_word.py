# -*- coding: UTF-8 -*-

# 答えをカウントアップ
ans = 0
# 入力
W = input().lower()
for _ in range(10**9+7):
    T = list(map(str, input().split()))
    for t in T:
        if t == 'END_OF_TEXT':
            # 出力
            print(ans)
            exit()
        if t.lower() == W:
            ans += 1