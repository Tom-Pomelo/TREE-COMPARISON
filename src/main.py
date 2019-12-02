from BST import *
from AVL import *
from BTree import *
from testcase import *
from matplotlib import pyplot as plt
from cycler import cycler
import os
import pickle


def plot():
    bst = []
    avl = []
    btree = []

    prefix_bst = 'BST'
    prefix_avl = 'AVL'
    prefix_btree = 'BTree'

    kv = [[prefix_bst, bst], [prefix_avl, avl], [prefix_btree, btree]]

    for t in kv:
        file_name = '../test/' + t[0] + '.pkl'
        with open(file_name, 'rb') as f:
            t[1] = pickle.load(f)
            f.close()

    plt.gca().set_prop_cycle(cycler('color', ['c', 'm', 'r']))

    nums = [10, 50, 100, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
    plt.scatter(nums, kv[0][1], marker = '^')

    plt.scatter(nums, kv[1][1], marker = '+')

    plt.scatter(nums, kv[2][1], marker = '*')

    plt.xlabel('Tree Size')
    plt.ylabel('Searches')
    plt.title('Num of Searches vs Tree Size')
    plt.legend(['Binary Search Tree', 'AVL Tree', 'B-Tree'], loc = 'upper left')
    plt.show()


def main():
    nums = [10, 50, 100, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
    generate_tree(nums)
    for opt in range(3):
        if opt == 0:
            T = BST()
        elif opt == 1:
            T = AVL()
        elif opt == 2:
            T = BTree()
        file_name = '../test/' + T.__class__.__name__ + '.pkl'
        if os.path.exists(file_name):
            continue
        res = []
        for n in nums:
            tree = extract_tree_element(n)
            for v in tree:
                T.insert(v)
            cnt = 0
            for v in tree:
                cnt += T.search(v)
            avg = cnt / n
            res.append(avg)
        print(res)
        with open(file_name, 'wb') as f:
            pickle.dump(res, f)
            f.close()
    plot()


if __name__ == '__main__':
    main()
    # T = AVL()
    # T.insert(5)
    # T.insert(10)
    # T.insert(8)
    # T.insert(3)
    # T.insert(15)
    # T.level_order()
