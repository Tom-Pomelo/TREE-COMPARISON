from queue import *


class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        pass

    def search_helper(self, node, val, cnt):
        if not node:
            return cnt + 1, False
        elif node.val == val:
            return cnt + 1, True
        elif node.val < val:
            return self.search_helper(node.right, val, cnt + 1)
        else:
            return self.search_helper(node.left, val, cnt + 1)

    def search(self, val):
        cnt = 0
        cnt, flag = self.search_helper(self.root, val, cnt)
        if flag:
            return cnt
        else:
            print('Element Not Found!')

    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.val)
            self.in_order(node.right)

    def level_order(self):
        q = Queue()
        q.put(self.root)
        while not q.empty():
            v = []
            for i in range(q.qsize()):
                n = q.get()
                v.append(n.val)
                if n.left:
                    q.put(n.left)
                if n.right:
                    q.put(n.right)
            print(v)

