__author__ = 'CLH'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            root = TreeNode(postorder[-1])
            index = inorder.index(postorder[-1])
            root.left = self.buildTree(inorder[:index],postorder[:index])
            root.right = self.buildTree(inorder[index+1:],postorder[index:-1])
            return root



if __name__ == "__main__":
    S = Solution()
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    tree = S.buildTree(inorder,postorder)
    print(tree)

