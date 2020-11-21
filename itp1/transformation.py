# -*- coding: UTF-8 -*-

# 入力
string = list(input())
q = int(input())
for _ in range(q):
    # 命令入力
    query = list(map(str, input().split()))
    # strの a 文字目から b 文字目までを p に置き換える
    if query[0] == 'replace':
        cnt = 0
        for i in range(int(query[1]), int(query[2])+1):
            string[i] = query[3][cnt]
            cnt += 1
    # strのの a 文字目から b 文字目までを逆順にする
    elif query[0] == 'reverse':
        rev = list(reversed(string[int(query[1]):int(query[2])+1]))
        cnt = 0
        for i in range(int(query[1]), int(query[2])+1):
            string[i] = rev[cnt]
            cnt += 1
    # strのの a 文字目から b 文字目までを出力する
    else:
        for i in string[int(query[1]):int(query[2])+1]:
            print(i, end='')
        print()