# -*- coding: UTF-8 -*-

# 辞書
dic = dict()
# 出力内容を保管
ans = []

# 入力
n = int(input())
for i in range(n):
    comm, string = map(str, input().split())
    if comm == 'insert':
        dic[string] = True
    else:
        if string in dic:
            ans.append('yes')
        else:
            ans.append('no')
# 出力
for i in ans:
    print(i)