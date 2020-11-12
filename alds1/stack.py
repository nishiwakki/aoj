# -*- coding: UTF-8 -*-

# 入力
# Reverse Polish Notation
rpn = list(map(str, input().split()))
stack = []
for i in rpn:
    if i == '+':
        stack.append(stack.pop() + stack.pop())
    elif i == '-':
        stack.append(- stack.pop() + stack.pop())
    elif i == '*':
        stack.append(stack.pop() * stack.pop())
    else:
        stack.append(int(i))
# 出力
print(stack[0])