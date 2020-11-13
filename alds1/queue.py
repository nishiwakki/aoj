# -*- coding: UTF-8 -*-

# Queueの標準ライブラリ
from collections import deque

# 入力
n, q = map(int, input().split())
# 入力される処理キュー
deq = deque()
# 処理完了したプロセスをプッシュ
ans = deque()
# 経過時間
elapsed = 0 
for i in range(n):
    name, time = map(str, input().split())
    deq.append([name, time])
# 処理キューがまだあるなら
while len(deq) > 0:
    proc = deq.popleft()
    name, time = proc[0], int(proc[1])
    # 処理残時間がqより長いか?
    if time > q:
        elapsed += q
        time -= q
        deq.append([name, str(time)])
    else:
        elapsed += time
        ans.append([name, elapsed])
# 出力
while len(ans) > 0:
    proc = ans.popleft()
    print(proc[0], proc[1])