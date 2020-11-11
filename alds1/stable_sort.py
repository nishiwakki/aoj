# -*- coding: UTF-8 -*-

from copy import deepcopy

# 隣同士のみの交換のため、大移動がない
# 順序がまばらになることがないためstable
def bubble_sort(A, N):
    flag = True
    while flag:
        flag = False
        for j in range(N-1, 0, -1):
            if int(A[j][1]) < int(A[j-1][1]):
                tmp = A[j]
                A[j] = A[j-1]
                A[j-1] = tmp
                flag = True

# 位置を無視して交換を行うため、
# 順序がまばらになる可能性アリ。not stable
def selection_sort(A, N):
    for i in range(0, N):
        minj = i
        for j in range(i, N):
            if int(A[j][1]) < int(A[minj][1]):
                minj = j
        if not minj == i:
            tmp = A[i]
            A[i] = A[minj]
            A[minj] = tmp

# 入力
N = int(input())
A1 = list(map(str, input().split()))
A2 = deepcopy(A1) # 選択ソート用

# 各数字(1~9)ごとの絵柄登場順
# 入力例1
# [[], [], ['D'], ['C'], ['H', 'S'], [], [], [], [], ['C']]
patCheck1 = [[] for _ in range(10)]
for a in A1:
    patCheck1[int(a[1])].append(a[0])
patCheck2 = deepcopy(patCheck1)
# ソート
bubble_sort(A1, N)
selection_sort(A2, N)
# 出力するansのフラグ
# True時、stable
ans1 = True
ans2 = True
# バブルソート
for a in A1:
    pat = a[0]
    num = int(a[1])
    if not patCheck1[num].pop(0) == pat:
        ans1 = False
        break
# 選択ソート
for a in A2:
    pat = a[0]
    num = int(a[1])
    if not patCheck2[num].pop(0) == pat:
        ans2 = False
        break
print(*A1)
if ans1:
    print('Stable')
else:
    print('Not stable')
print(*A2)
if ans2:
    print('Stable')
else:
    print('Not stable')