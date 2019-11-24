from queue import *


class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        pass

    def search_helper(self, node, val):
        if not node:
            return False
        elif node.val == val:
            return True
        elif node.val < val:
            return self.search_helper(node.right, val)
        else:
            return self.search_helper(node.left, val)

    def search(self, val):
        flag = self.search_helper(self.root, val)
        if flag:
            print('Found!')
        else:
            print('Not Found!')

    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.val)
            self.in_order(node.right)

    def level_order(self):
        vec = []
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
            vec.append(v)
        print(vec)
