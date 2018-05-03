# -*- coding -*-
__author__ = 'CLH'


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        else:
            ans = []
            path = str(root.val)
            self._binaryTreePaths(root,ans,path)
            return ans


    def _binaryTreePaths(self,node,ans,path):
        if not node.left and not node.right:
            print path
            ans.append(path)
            return
        if node.left:
            self._binaryTreePaths(node.left,ans,path+"->"+str(node.left.val))
        if node.right:
            self._binaryTreePaths(node.right,ans,path+"->"+str(node.right.val))