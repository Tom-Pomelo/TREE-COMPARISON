from TreeNode import *


def height(node):
    if not node:
        return -1
    else:
        return node.height


def adjust_height(node):
    if not node:
        return
    node.height = max(height(node.left), height(node.right)) + 1


def balance_factor(node):
    if not node:
        return 0
    return height(node.left) - height(node.right)


def left_left_rotation(node):
    pass


def right_right_rotation(node):
    pass


def left_right_rotation(node):
    pass


def right_left_rotation(node):
    pass


def balance(node):
    if balance_factor(node) > 1:
        if balance_factor(node.left) > 0:
            left_left_rotation(node)
        else:
            left_right_rotation(node)
    elif balance_factor(node) < -1:
        if balance_factor(node.right) < 0:
            right_right_rotation(node)
        else:
            right_left_rotation(node)


class AVL(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        n = Node(val)
        if not self.root:
            self.root = n
        else:
            curr = self.root
            while True:
                if val < curr.val:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = n
                        n.parent = curr
                        break
                elif val > curr.val:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = n
                        n.parent = curr
                        break
                else:
                    curr.val = n.val
                adjust_height(curr)
                balance(curr)

    def search(self, val):
        pass

    def traverse(self):
        pass
