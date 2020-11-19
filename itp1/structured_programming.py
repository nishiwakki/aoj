# -*- coding: UTF-8 -*-

def call(n):
    # 返値変数
    ret = ''
    i = 1
    while i <= n:
        x = i
        # 3の倍数か?
        if x % 3 == 0:
            ret += ' ' + str(i)
        # iに3が含まれるか?
        elif str(x).count('3') > 0:
            ret += ' ' + str(i)
        i += 1
    return ret 

# 入力
N = int(input())
# 出力
print(call(N))