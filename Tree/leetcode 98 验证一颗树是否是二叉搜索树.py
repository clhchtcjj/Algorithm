__author__ = 'CLH'
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        lastnode = [None]
        if root is None:
            return True
        return self.inOrderBST(root,lastnode)

    def inOrderBST(self, node, lastnode):
        if node is None:
            return True
        result = True
        if node.left:
            result = self.inOrderBST(node.left,lastnode)
        if result:
            if lastnode[0] is not None and lastnode[0].val >= node.val:
                result = False
                print 1
        lastnode[0] = node
        if node.right and result:
            result = self.inOrderBST(node.right,lastnode)
        return result