# -*- coding: UTF-8 -*-

# 入力
n = int(input())
R0 = int(input())
R1 = int(input())
# 0 ~ i番目までの入力Rの最低値
# R0, R1の小さい方を初期値とする
minR = min(R0, R1)
# 答え（価格の差の最大値）
ans = R1 - R0
# n-2回繰り返し(n=2ならpass)
for i in range(n-2):
    R = int(input())
    if R - minR > ans:
        ans = R - minR
    minR = min(minR, R)
print(ans)