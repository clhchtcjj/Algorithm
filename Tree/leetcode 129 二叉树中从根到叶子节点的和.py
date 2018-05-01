# -*- coding:utf-8 -*-
__author__ = 'CLH'

# 思路：层次遍历法
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import Queue
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q_node = Queue.Queue()
        q_num = Queue.Queue()
        q_node.put(root)
        q_num.put(root.val)
        sum = 0
        while not q_node.empty():
            lens = q_node.qsize()
            for i in range(lens):
                node = q_node.get()
                val = q_num.get()
                if not node.left and not node.right:
                    sum += val
                if node.left:
                    q_node.put(node.left)
                    q_num.put(val*10+node.left.val)
                if node.right:
                    q_node.put(node.right)
                    q_num.put(val*10+node.right.val)
        return sum
'''
class Solution(object):

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        path_sum = [0]
        self.sum = 0
        self.sum_rec(root, 0)
        return self.sum

    def sum_rec(self, n, r_l_sum):
        if not n:
            return

        r_l_sum = r_l_sum*10 + n.val

        if not n.left and not n.right:
            self.sum += r_l_sum
            return

        self.sum_rec(n.left, r_l_sum)
        self.sum_rec(n.right, r_l_sum)

'''