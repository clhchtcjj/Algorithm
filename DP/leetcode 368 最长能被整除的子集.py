# -*- coding: utf-8 -*-
__author__ = 'CLH'


class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        nums.sort()
        if n < 1:
            return []
        if n == 1:
            return nums
        dp = [nums[0]]
        pre = [-1]
        lens = [1]
        for i in range(1,n):
            max_num = -1
            max_index = -1
            for j in range(i):
                if nums[i] % dp[j] == 0:
                    if max_num < lens[j]:
                        max_num = lens[j]
                        max_index = j
            if max_index != -1:
                pre.append(max_index)
                dp.append(nums[i])
                lens.append(lens[max_index]+1)
            else:
                pre.append(-1)
                dp.append(nums[i])
                lens.append(1)
            # print "dp",dp
            # print "pre",pre
        ans_last = n-1
        max_len = -1
        for i,l in enumerate(lens):
            if l > max_len:
                max_len = l
                ans_last = i
        l = []
        while ans_last != -1:
            l.append(nums[ans_last])
            ans_last = pre[ans_last]
        return l


if __name__ == "__main__":
    S = Solution()
    print(S.largestDivisibleSubset([4,8,10,240]))