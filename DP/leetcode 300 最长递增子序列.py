# -*- coding: utf-8 -*-
__author__ = 'CLH'


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # hash_dp = {}
        # n = len(nums)
        # keys = []
        # ans = -1
        # for i in range(n):
        #     index = self.binarySearch(keys,nums[i])
        #     if index == 0:
        #         hash_dp[nums[i]] = 1
        #     max_len = -1
        #     for key in keys[0:index]:
        #         if hash_dp[key] > max_len:
        #             max_len = hash_dp[key]
        #     hash_dp[nums[i]] = max_len + 1
        #     if ans < max_len + 1:
        #         ans = max_len + 1
        #     keys.append(nums[i])
        #     keys.sort()
        # return ans
        # =================================================
        # B[i] 表示长度为i的递增子序列的末尾字符
        B = [-float('inf')]
        n = len(nums)
        if n == 0:
            return 0
        B.append(nums[0])
        for i in range(1,n):
            pos = self.binarySearch(B,nums[i])
            # print B
            # print nums[i], pos
            if pos == len(B):
                B.append(nums[i])
            else:
                B[pos] = nums[i]
        return len(B)-1



    def binarySearch(self,nums,target):
        if len(nums) == 0:
            return 0
        i = 0
        j = len(nums)-1
        while i <= j:
            mid = i + (j - i) // 2
            if nums[mid] < target: i = mid + 1
            if nums[mid] > target: j = mid -1
            if nums[mid] == target: return mid
        return i