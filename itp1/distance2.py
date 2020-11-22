# -*- coding: UTF-8 -*-

# 入力
n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

# p=1: マンハッタン距離
ans1 = 0
for i in range(n):
    ans1 += abs(x[i]-y[i])
# p=2: ユークリッド距離
ans2 = 0
for i in range(n):
    ans2 += abs(x[i]-y[i]) ** 2
ans2 = ans2 ** 0.5
# p=3
ans3 = 0
for i in range(n):
    ans3 += abs(x[i]-y[i]) ** 3
ans3 = ans3 ** (1.0/3.0)
# p=∞: チェビシェフ距離
ans4 = 0
for i in range(n):
    ans4 = max(ans4, abs(x[i]-y[i]))
# 出力
print(ans1)
print(ans2)
print(ans3)
print(ans4)