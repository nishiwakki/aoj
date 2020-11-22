# -*- coding: UTF-8 -*-

import random

class Dice3:
    allAct = ['S', 'N', 'E', 'W']

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
        for i in range(10**9+7):
            idx = random.randint(0, 3)
            self.roll(Dice3.allAct[idx])
            if self.to == top and self.ba == back:
                return self.ri
    
    def isSame(self, label):
        for i in range(10**5):
            idx = random.randint(0, 3)
            self.roll(Dice3.allAct[idx])
            if self.to == label[0] and self.ba == label[1] \
                and self.ri == label[2] and self.le == label[3] \
                and self.fr == label[4] and self.bo == label[5]:
                return True
        return False

# 入力
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
# インスタンス化
dice = Dice3(l1)
if dice.isSame(l2):
    print('Yes')
else:
    print('No')