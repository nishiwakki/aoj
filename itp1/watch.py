# -*- coding: UTF-8 -*-

# 入力
S = int(input())
# 時間(3600s)で割る
h = S // 3600
S -= 3600 * h
# 時間(60s)で割る
m = S // 60
S -= 60 * m
# 出力
print(str(h) + ':' + str(m) + ':' + str(S))