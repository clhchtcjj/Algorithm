__author__ = 'CLH'


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        K = [k]
        # print K
        if not root:
            return None
        return self._kthSmallest(root,K)

    def _kthSmallest(self,root,K):
        if not root:
            return None
        result = None
        result = self._kthSmallest(root.left,K)
        if result is None:
            # print K
            K[0] = K[0] - 1
            if K[0] == 0:
                # print root.val
                result = root.val
        if result is None:
            result = self._kthSmallest(root.right,K)
        return result