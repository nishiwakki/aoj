# -*- coding: UTF-8 -*-

# 得点変数
taro = 0
hana = 0
# 入力
n = int(input())
for _ in range(n):
    s1, s2 = map(str, input().split())
    # 辞書順比較
    if s1 > s2:
        taro += 3
    elif s1 < s2:
        hana += 3
    else:
        taro += 1
        hana += 1
# 出力
print(taro, hana)