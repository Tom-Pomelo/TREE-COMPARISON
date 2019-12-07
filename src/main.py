from BST import *
from AVL import *
from BTree import *
from testcase import *
from matplotlib import pyplot as plt
from cycler import cycler
import math
import os
import pickle
from scipy import optimize
import numpy as np


def linear_func(x, k, b):
    return k * x + b


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

    tree_size = [10, 50, 100, 500, 1000, 1500,
                 2000, 2500, 3000, 3500, 4000, 4500, 5000]
    log_tree_size = list(map(math.log, tree_size))

    file_1 = '../fig/original.png'
    file_2 = '../fig/log.png'

    if not os.path.exists(file_1):
        plt.gca().set_prop_cycle(cycler('color', ['c', 'm', 'y']))
        plt.scatter(tree_size, kv[0][1], marker='^')
        plt.scatter(tree_size, kv[1][1], marker='+')
        plt.scatter(tree_size, kv[2][1], marker='*')
        plt.xlabel('Tree Size')
        plt.ylabel('Num of Nodes Examined')
        plt.title('Num of Nodes Examined vs Tree Size')
        plt.legend(['Binary Search Tree', 'AVL Tree',
                    'B-Tree'], loc='upper left')
        plt.savefig('../fig/original.png')
        plt.close()
    if not os.path.exists(file_2):
        plt.gca().set_prop_cycle(cycler('color', ['c', 'm', 'y']))
        plt.scatter(log_tree_size, kv[0][1], marker='^')
        plt.scatter(log_tree_size, kv[1][1], marker='+')
        plt.scatter(log_tree_size, kv[2][1], marker='*')

        a, b = optimize.curve_fit(linear_func, log_tree_size, kv[1][1])[0]
        print(a, b)
        x = np.arange(-2, 8, 0.1)
        y = a * x + b
        plt.plot(x, y, "m")

        a, b = optimize.curve_fit(linear_func, log_tree_size, kv[2][1])[0]
        print(a, b)
        x = np.arange(-2, 8, 0.1)
        y = a * x + b
        plt.plot(x, y, "y")

        plt.xlabel('Log(Tree Size)')
        plt.ylabel('Num of Nodes Examined')
        plt.title('Num of Nodes Examined vs Log(Tree Size)')
        plt.legend(['Binary Search Tree', 'AVL Tree',
                    'B-Tree'], loc='upper left')
        plt.savefig('../fig/log.png')
        plt.close()


def main():
    nums = [10, 50, 100, 500, 1000, 1500, 2000,
            2500, 3000, 3500, 4000, 4500, 5000]
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
        with open(file_name, 'wb') as f:
            pickle.dump(res, f)
            f.close()
    plot()


if __name__ == '__main__':
    main()
