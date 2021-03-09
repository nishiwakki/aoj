# -*- coding: UTF-8 -*-

# INFINITY
INF = 5 * 10 ** 4
# 入力
n, m = map(int, input().split())
c = list(map(int, input().split()))
# DP準備
dp = [INF] * (n+10001)
dp[0] = 0
# DP
for i in range(n-1):
    for val in c:
        dp[i+val] = min(dp[i+val], dp[i]+1)
# 出力
print(dp[n])