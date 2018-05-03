# -*- coding: utf-8 -*-
__author__ = 'CLH'


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        table = {}
        ans = []
        self._findFrequentTreeSum(root,table)
        ftimes = max(table.values())
        for k,v in table.items():
            if v == ftimes:
                ans.append(k)
        return ans


    def _findFrequentTreeSum(self,node,table):
        if not node:
            return 0
        leftsum = self._findFrequentTreeSum(node.left,table)
        rightsum = self._findFrequentTreeSum(node.right,table)
        currsum = leftsum+rightsum+node.val
        table[currsum] = table.get(currsum,0) + 1
        return currsum