# -*- coding: UTF-8 -*-

# 素数判定する関数
# Trueのとき、nは素数
def is_prime(n):
    # 1は素数でない
    if n == 1:
        return False
    # 2からcert(ルートn+1)までで割り切れるかチェック
    for k in range(2, int(n**0.5)+1):
        if n % k == 0:
            return False
    return True

# 出力値（入力に含まれる素数の数）
primeCnt = 0
# 入力
n = int(input())
for i in range(n):
    v = int(input())
    if is_prime(v):
        primeCnt += 1
print(primeCnt)