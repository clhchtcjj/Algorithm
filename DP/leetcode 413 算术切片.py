# -*- coding:utf-8 -*-
__author__ = 'CLH'

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n < 3:
            return 0
        count = 0
        added = 0
        for i in range(2,n):
            if A[i-1]-A[i]==A[i-2]-A[i-1]:
                added += 1
                count += added
            else:
                added = 0
        return count