# -*- coding: UTF-8 -*-

# 複数行入力
import sys

# 出現回数をカウント
cntCha = [0] * 26
# 入力
string = sys.stdin.readlines()
# 1行ずつ
for line in string:
    # 1文字ずつ
    for c in line:
        # 大文字は小文字に
        cc = c.lower()
        # 97='a' ~ 122='z'
        if 97 <= ord(cc) <= 122:
            cntCha[ord(cc)-97] += 1
# 出力
for c, cnt in enumerate(cntCha):
    print(chr(c+97), ':', str(cnt))