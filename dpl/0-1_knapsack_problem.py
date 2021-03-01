# -*- coding: UTF-8 -*-

# N, W入力
N, W = map(int, input().split())
# DPを0で初期化
dp = [[0] * (W+1) for _ in range(N+1)]
# 各品物について
for i in range(1, N+1):
    # 品物入力
    v, w = map(int, input().split())
    # 各重さについて(貰うDP)
    for j in range(1, W+1):
        if j-w >= 0:
            # i-1からの遷移のみ
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
        else:
            dp[i][j] = dp[i-1][j]
    print(dp[i])
# 出力
print(dp[N][W])