# -*- coding: UTF-8 -*-

# 公舎4棟の情報
A = [[[0 for room in range(10)] for floor in range(3)] for building in range(4)]
# 入力
n = int(input())
for i in range(n):
    b, f, r, v = map(int, input().split())
    A[b-1][f-1][r-1] += v
# 出力
output = ''
for idx, building in enumerate(A):
    for floor in building:
        for room in floor:
            output += ' ' + str(room)
        output += '\n'
    if not idx == 3:
        output += '#' * 20 + '\n'
print(output.rstrip('\n'))