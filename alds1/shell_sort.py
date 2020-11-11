# -*- coding: UTF-8 -*-

# 一定の間隔 g だけ離れた要素のみを対象とした挿入ソート
def insertion_sort(A, n, g):
    cnt = 0
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j -= g
            cnt += 1
        A[j+g] = v
    return cnt

# シェルソート 
def shell_sort(A, n):
    G = []
    h = 1
    while True:
        if h > n:
            break
        G.append(h)
        # hn+1 = 3hn + 1 がベスト
        h = 3*h + 1
    m = len(G)
    # 大きい値から縮めていくためreverse
    G.reverse()
    cnt = 0
    for i in range(m):
        cnt += insertion_sort(A, n, G[i])
    return m, G, cnt

# 入力
n = int(input())
A = [0] * n
for i in range(n):
    A[i] = int(input())

m, G, cnt = shell_sort(A, n)
# 出力
print(m)
print(*G)
print(cnt)
for i in A:
    print(i)