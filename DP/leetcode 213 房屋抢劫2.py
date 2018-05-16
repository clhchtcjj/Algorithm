# -*- coding: utf-8 -*-
__author__ = 'CLH'


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 1:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        dp_1 = nums[0:2]
        dp_2 = [0,nums[1]]
        for i in range(2, n):
            dp_1.append(max(dp_1[0:i-1])+nums[i])
            dp_2.append(max(dp_2[0:i-1])+nums[i])
        if dp_1[-1] >= dp_1[-2]:
            return max(dp_2[-1], dp_1[-2])
        else:
            return max(dp_1[-1], dp_1[-2])




