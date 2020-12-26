# -*- coding: UTF-8 -*-

# 入力
n = int(input())
a = list(map(int, input().split()))
# チェックするリスト要素の前要素の値を保持
prev_a = a[0]
ans = [prev_a]
for i in range(1, n):
    # prev_aと同値の場合
    if not prev_a == a[i]:
        # ansに追加
        ans.append(a[i])
        # prev_aを更新
        prev_a = a[i]
# 出力
print(*ans)