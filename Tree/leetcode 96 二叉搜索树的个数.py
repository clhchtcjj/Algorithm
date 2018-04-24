# -*- coding:utf-8 -*-
__author__ = 'CLH'


# 思路：卡特兰数
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def numTreesI(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 1
        for i in range(n+1,2*n+1):
            ans = ans * i / (i-n)
        return ans / (n+1)

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.dfs(1, n+1)

    def dfs(self, start, end):
        if start == end:
            return [None]
        result = []
        for i in xrange(start, end):
            for l in self.dfs(start, i):
                for r in self.dfs(i+1, end):
                    node = TreeNode(i)
                    node.left, node.right  = l, r
                    result.append(node)
        return result