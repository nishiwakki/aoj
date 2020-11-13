# -*- coding: UTF-8 -*-

from collections import deque
import sys

# 入力高速化
input = sys.stdin.readline
# 双方向連結リスト
dll = deque()

n = int(input())
for i in range(n):
    comm = list(map(str, input().split()))
    if comm[0] == 'insert':
        dll.appendleft(comm[1])
    elif comm[0] == 'delete':
        try:
            dll.remove(comm[1])
        # そのような要素が存在しない場合は何もしない
        except ValueError:
            pass
    elif comm[0] == 'deleteFirst':
        dll.popleft()
    else:
        dll.pop()
# 出力
print(*dll)