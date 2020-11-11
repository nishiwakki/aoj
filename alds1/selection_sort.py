# -*- coding: UTF-8 -*-

# N個の要素を含む0-オリジンの配列A
def selection_sort(A, N):
    changeCnt = 0
    for i in range(0, N):
        # 整列済みでない配列の先頭idxを最小としておく
        minj = i
        # i番目~N-1番目までの最初を選択
        for j in range(i, N):
            if A[j] < A[minj]:
                minj = j
        # iとminjが異なっていた場合
        # 整列済みでない配列の先頭idxが最小でなかった場合
        if not minj == i:
            tmp = A[i]
            A[i] = A[minj]
            A[minj] = tmp
            changeCnt += 1
    return changeCnt

# 入力
N = int(input())
A = list(map(int, input().split()))

ans = selection_sort(A, N)
# 出力
#print(' '.join(map(str, A)))
print(*A)
print(ans)