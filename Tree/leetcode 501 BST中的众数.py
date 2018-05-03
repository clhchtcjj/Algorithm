# -*- coding:utf-8 -*-
__author__ = 'CLH'


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import Queue
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return None
        q = Queue.Queue()
        q.put(root)
        count = {}
        while not q.empty():
            lens = q.qsize()
            for i in range(lens):
                node = q.get()
                count[node.val] = count.get(node.val,0) + 1
                if node.left: q.put(node.left)
                if node.right: q.put(node.right)

        modes = max(count.values())
        ans = []
        for k,v in count:
            if v == modes:
                ans.append(k)
        return ans


