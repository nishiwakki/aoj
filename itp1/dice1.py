# -*- coding: UTF-8 -*-

class Dice1:
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

# 入力
l = list(map(int, input().split()))
q = list(input())
# インスタンス化
dice = Dice1(l)
for i in q:
    dice.roll(i)
# 出力
print(dice.output())