# -*- coding: UTF-8 -*-

# N個の要素を含む0-originの配列A
def insertion_sort(A, N):
    for i in range(1, N):
        # 挿入する値vを取得
        v = A[i]
        # 整列済み範囲の最後idxを取得
        j = i - 1
        # 整列済み範囲の後ろから
        while j >= 0 and A[j] > v:
            # 大きい値は後ろにpushしていく
            A[j+1] = A[j]
            j -= 1
        # 適切な場所に挿入
        A[j+1] = v
        output(A, N)

# 出力の形式
def output(arr, N):
    for i in range(N):
        if i == N-1:
            print(arr[i])
        else:
            print(arr[i], end=' ')

n = int(input())
a = list(map(int, input().split()))
output(a, n)
insertion_sort(a, n)