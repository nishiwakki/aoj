# -*- coding: UTF-8 -*-

# 入力
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
ans = None
for i in range(min(n, m)):
    if a[i] < b[i]:
        ans = 1
    elif a[i] > b[i]:
        ans = 0
    if not ans is None:
        break
# 出力
# Sample Input 3 のような場合
if ans is None:
    if n < m:
        print(1)
    else:
        print(0)
else:
    print(ans)