# -*- coding: UTF-8 -*-

# Nodeクラスを定義
class Node:
    def __init__(self, prev_node, next_node, id, val):
        self.prev = prev_node
        self.next = next_node
        self.id = id
        self.val = val

class LinkedList:
    def __init__(self):
        # 先頭ダミーノードの作成
        begin_node = Node(None, None, 0, -10**9-1)
        # 後尾ダミーノードの作成
        end_node = Node(None, None, 1, 10**9+1)
        # 先頭ダミーノードの次は後尾ダミーノード
        begin_node.next = end_node
        # 後尾ダミーノードの前は先頭ダミーノード
        end_node.prev = begin_node
        # ノード管理(dictで管理)
        self.Nodes = {0: begin_node, 1: end_node}
        # 次にinsertされるノードのid
        self.id = 2
        # カーソルを後尾ダミーノードに
        self.cursor = self.Nodes[1]
    
    def insert(self, x):
        tmp_node = Node(self.cursor.prev, self.cursor, self.id, x)
        # カーソル前後の付け替え
        self.cursor.prev.next = tmp_node
        self.cursor.prev = tmp_node
        # ノード管理のdictに追加
        self.Nodes[self.id] = tmp_node
        # insert後のカーソルは追加要素を指す
        self.cursor = tmp_node
        self.id += 1
    
    def move(self, d):
        # ノードのprev, nextを辿ってカーソルを動かす
        if d < 0:
            for i in range(-d):
                self.cursor = self.cursor.prev
        else:
            for i in range(d):
                self.cursor = self.cursor.next

    def erase(self):
        # ノードのprev, nextを付け替え
        self.cursor.prev.next = self.cursor.next
        self.cursor.next.prev = self.cursor.prev
        # ノードを削除
        del self.Nodes[self.cursor.id]
        # カーソルを削除対象の次に移行
        self.cursor = self.cursor.next
    
    def print_all_nodes(self):
        print_out = ''
        # 先頭までカーソルを戻す
        while self.cursor.prev is not None:
            self.cursor = self.cursor.prev
        # 先頭ダミーノードは出力しない
        self.cursor = self.cursor.next
        while self.cursor.next is not None:
            print_out += f'{self.cursor.val}\n'
            self.cursor = self.cursor.next
        return print_out.rstrip('\n')


L = LinkedList()
# 入力
q = int(input())
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        # insert(x)
        L.insert(query[1])
    elif query[0] == 1:
        # move(d)
        L.move(query[1])
    else:
        # erase()
        L.erase()
# 出力
print(L.print_all_nodes())