# -*- coding: utf-8 -*-
__author__ = 'CLH'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.ans = []
        self.path = []

    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        self.path.append(root.val)
        return self.fun(root,expectNumber-root.val)

    def fun(self,root, expectNumber):
        if expectNumber == 0 and root.left == None and root.right == None:
            self.ans.append(list(self.path))
            return
        elif expectNumber < 0 or (root.left == None and root.right == None):
            return
        else:
            if root.left:
                self.path.append(root.left.val)
                self.fun(root.left,expectNumber-root.left.val)
                self.path.pop()
            if root.right:
                self.path.append(root.right.val)
                self.fun(root.right,expectNumber-root.right.val)
                self.path.pop()
        return self.ans

'''
class Solution:
    def func(self, node, sum, path):
        if sum > self.expectNumber:
            return
        if node.left is None and node.right is None:#没有了节点了，不然还有0节点。
            if sum == self.expectNumber:
                self.result.append(path)
            return
        if node.left is not None:
            self.func(node.left, sum + node.left.val, path + [node.left.val])
        if node.right is not None:
            self.func(node.right, sum + node.right.val, path + [node.right.val])
    def FindPath(self, root, expectNumber):
        if root is None:
            return []
        self.expectNumber = expectNumber
        self.result = []
        self.func(root, root.val, [root.val])
        return self.result
'''
if __name__ == "__main__":
    root = TreeNode(1)
    # root.left = TreeNode(5)
    # root.right = TreeNode(12)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(7)

    S = Solution()
    S.FindPath(root,1)
    print(S.ans)



