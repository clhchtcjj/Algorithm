# -*- coding: utf-8 -*-
__author__ = 'CLH'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():

    def firstOrderEncode(self,root,string):
        if not root:
            string += "#,"
            return string
        string += str(root.val)+","
        string = self.firstOrderEncode(root.left,string)
        string = self.firstOrderEncode(root.right,string)
        return string

    def firstOrderDecode(self,string):
        if string == "":
            return None,string
        if string[0] == "#":
            return None, string
        else:
            root = TreeNode(string[0])
            root.left,string = self.firstOrderDecode(string[1:])
            root.right,string = self.firstOrderDecode(string[1:])
            return root,string


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return self.firstOrderEncode(root,[])

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        root =  TreeNode
        root,string = self.firstOrderDecode(data)
        return root

    def firstOrderEncode(self,root,string):
        if not root:
            return string

        if root.left:
            string = self.firstOrderEncode(root.left,string)
        else:
            string.append(None)
        string.append(root.val)
        if root.right:
            string = self.firstOrderEncode(root.right,string)
        else:
            string.append(None)
        return string

    def firstOrderDecode(self,string):
        if len(string) == 0:
            return None,string
        else:
            root = TreeNode(None)
            if string[0] is None:
                return None,string
            root.left,string = self.firstOrderDecode(string)
            root.val = string[0]
            root.right,string = self.firstOrderDecode(string[1:])
            return root,string


if __name__ == "__main__":
    root = TreeNode(1)
    # root.left = TreeNode(5)
    root.right = TreeNode(12)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(7)
    # root.right.left = TreeNode(8)
    root.right.right = TreeNode(13)
    # root = None
    S = Codec()
    string = S.serialize(root)
    print(string)
    tree,_ = S.firstOrderDecode(string)
    string1 = S.serialize(tree)
    print(string1)