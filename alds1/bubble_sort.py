# -*- coding: UTF-8 -*-

# N個の要素を含む0-オリジンの配列A
# 昇順にバブルソート 
def bubble_sort(A, N):
    changeCnt = 0
    # 逆の隣接要素が存在する
    flag = True
    while flag:
        flag = False
        for j in range(N-1, 0, -1):
            # 後ろの要素が前の要素より小さいか?
            if A[j] < A[j-1]:
                tmp = A[j]
                A[j] = A[j-1]
                A[j-1] = tmp
                flag = True
                # 交換回数 + 1
                changeCnt += 1
    return changeCnt

# 入力
N = int(input())
A = list(map(int, input().split()))
# 出力
ans = bubble_sort(A, N)
print(' '.join(map(str, A)))
print(ans)