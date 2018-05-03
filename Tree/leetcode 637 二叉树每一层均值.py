# -*- coding:utf-8 -*-
__author__ = 'CLH'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        q = [root]
        ans = []
        while len(q) != 0:
            tmp_q = []
            current = []
            for node in q:
                current.append(node.val)
                if node.left: tmp_q.append(node.left)
                if node.right: tmp_q.append(node.right)
            ans.append(sum(current)*1.0/len(current))
            q = tmp_q
        return ans


