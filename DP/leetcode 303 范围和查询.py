# -*- coding: utf-8 -*-
__author__ = 'CLH'



class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.running_sum = {-1:0}
        for i,num in enumerate(nums):
            self.running_sum[i] = self.running_sum[i-1] + num

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.running_sum[j] - self.running_sum[i-1]




# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)