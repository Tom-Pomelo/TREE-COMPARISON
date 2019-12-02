from queue import *


def get_index(l, val):
    l_copy = l.copy()
    l_copy.append(val)
    l_copy.sort()
    return l_copy.index(val)


class BNode(object):
    def __init__(self, tree, contents = None, children = None):
        self.tree = tree
        self.contents = contents or []
        self.children = children or []

    def lateral(self, parent, parent_index, destination, destination_index):
        if parent_index > destination_index:
            destination.contents.append(parent.contents[destination_index])
            parent.contents[destination_index] = self.contents.pop(0)
            if self.children:
                destination.children.append(self.children.pop(0))
        else:
            destination.contents.insert(0, parent.contents[parent_index])
            parent.contents[parent_index] = self.contents.pop()
            if self.children:
                destination.children.insert(0, self.children.pop())

    def shrink(self, ancestors):
        parent = None

        if ancestors:
            parent, parent_index = ancestors.pop()
            if parent_index:
                left_sib = parent.children[parent_index - 1]
                if len(left_sib.contents) < self.tree.order:
                    self.lateral(parent, parent_index, left_sib, parent_index - 1)
                    return
            if parent_index + 1 < len(parent.children):
                right_sib = parent.children[parent_index + 1]
                if len(right_sib.contents) < self.tree.order:
                    self.lateral(parent, parent_index, right_sib, parent_index + 1)
                    return

        sibling, push = self.split()

        if not parent:
            parent, parent_index = self.tree.BRANCH(self.tree, children = [self]), 0
            self.tree.root = parent

        parent.contents.insert(parent_index, push)
        parent.children.insert(parent_index + 1, sibling)
        if len(parent.contents) > parent.tree.order:
            parent.shrink(ancestors)

    def split(self):
        center = len(self.contents) // 2
        median = self.contents[center]
        sibling = type(self)(
            self.tree,
            self.contents[center + 1:],
            self.children[center + 1:])
        self.contents = self.contents[:center]
        self.children = self.children[:center + 1]
        return sibling, median

    def insert(self, index, val, ancestors):
        self.contents.insert(index, val)
        if len(self.contents) > self.tree.order:
            self.shrink(ancestors)


class BTree(object):
    BRANCH = LEAF = BNode

    def __init__(self, order = 3):
        self.order = order
        self.root = BNode(self)

    def get_ancestors(self, val):
        current = self.root
        ancestors = []

        while getattr(current, 'children', None):
            index = get_index(current.contents, val)
            ancestors.append((current, index))
            if index < len(current.contents) and current.contents[index] == val:
                return ancestors
            current = current.children[index]

        index = get_index(current.contents, val)
        ancestors.append((current, index))
        return ancestors

    def insert(self, val):
        ancestors = self.get_ancestors(val)
        node, index = ancestors[-1]
        while getattr(node, 'children', None):
            node = node.children[index]
            index = get_index(node.contents, val)
            ancestors.append((node, index))
        node, index = ancestors.pop()
        node.insert(index, val, ancestors)

    def search_helper(self, node, val, cnt):
        if not node:
            return cnt + 1, False
        if val in node.contents:
            return cnt + 1, True
        index = get_index(node.contents, val)
        return self.search_helper(node.children[index], val, cnt + 1)

    def search(self, val):
        cnt = 0
        cnt, flag = self.search_helper(self.root, val, cnt)
        if flag:
            return cnt
        else:
            print('Element Not Found!')

    def level_order(self):
        q = Queue()
        q.put(self.root)
        while not q.empty():
            v = []
            for i in range(q.qsize()):
                n = q.get()
                v.append(n.contents)
                for n in n.children:
                    q.put(n)
            print(v)
