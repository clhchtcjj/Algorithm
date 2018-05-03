# -*- coding: utf-8 -*-
__author__ = 'CLH'


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# class Solution(object):
#     def rob(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if not root:
#             return 0
#         val = 0
#         if root.left:
#             val += self.rob(root.left.left) + self.rob(root.left.right)
#         if root.right:
#             val += self.rob(root.right.left) + self.rob(root.right.right)
#         return max(root.val + val, self.rob(root.left)+self.rob(root.right))

# #  用hashmap加速
# class Solution(object):
#     def rob(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if not root:
#             return 0
#         table = {}
#         return self._rob(root,table)
#
#     def _rob(self,node,table):
#         if not node:
#             return 0
#         if table.get(node) is not None:
#             return table[node]
#         val = 0
#         if node.left:
#             val += self.rob(node.left.left) + self.rob(node.left.right)
#         if node.right:
#             val += self.rob(node.right.left) + self.rob(node.right.right)
#         ans = max(node.val + val, self.rob(node.left)+self.rob(node.right))
#         table[node] = ans
#         return ans

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def _rob(node):
            if node is None: return [0, 0]
            left = _rob(node.left)
            right = _rob(node.right)
            return node.val + left[1] + right[1], max(left[0], left[1]) + max(right[0], right[1])

        res = _rob(root)
        return max(res[0], res[1])