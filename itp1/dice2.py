# -*- coding: UTF-8 -*-

import random

class Dice2:
    def __init__(self, label):
        self.to, self.ba, self.ri = label[0], label[1], label[2]
        self.le, self.fr, self.bo = label[3], label[4], label[5]

    def roll(self, act):
        if act == 'S':
            self.to, self.ba, self.fr, self.bo \
                = self.fr, self.to, self.bo, self.ba
        elif act == 'N':
            self.to, self.ba, self.fr, self.bo \
                = self.ba, self.bo, self.to, self.fr
        elif act == 'E':
            self.to, self.le, self.bo, self.ri \
                = self.le, self.bo, self.ri, self.to
        elif act == 'W':
            self.to, self.le, self.bo, self.ri \
                = self.ri, self.to, self.le, self.bo

    def output(self):
        return self.to
    
    def randomRoll(self, top, back):
        allAct = ['S', 'N', 'E', 'W']
        for i in range(10**9+7):
            idx = random.randint(0, 3)
            self.roll(allAct[idx])
            if self.to == top and self.ba == back:
                return self.ri

# 入力
l = list(map(int, input().split()))
q = int(input())
# インスタンス化
dice = Dice2(l)
ans = []
for i in range(q):
    t, f = map(int, input().split())
    ans.append(dice.randomRoll(t, f))
# 出力
for i in ans:
    print(i)