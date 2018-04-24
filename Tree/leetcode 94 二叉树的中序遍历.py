__author__ = 'CLH'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        self._inorderTraversal(root,ans)
        return ans
    def _inorderTraversal(self,root,ans):
        if root is None:
            return
        if root.left:
            self._inorderTraversal(root.left,ans)
        ans.append(root.val)
        if root.right:
            self._inorderTraversal(root.right,ans)