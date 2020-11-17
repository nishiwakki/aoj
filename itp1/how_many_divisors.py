# -*- coding: UTF-8 -*-

# 入力
a, b, c = map(int, input().split())
ans = 0
for i in range(a, b+1):
    if c % i == 0:
        ans += 1
# 出力
print(ans)