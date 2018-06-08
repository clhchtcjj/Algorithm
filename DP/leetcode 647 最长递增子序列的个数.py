# -*- coding: utf-8 -*-
__author__ = 'CLH'


class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        dp = [0 for _ in range(n)]
        len_num = [0 for _ in range(n)]
        dp[0] = 1
        len_num[0] = 1
        for i in range(1,n):
            dp[i] = 1

            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j]+1,dp[i])
            for j in range(i):
                if dp[j] == dp[i]-1 and nums[i] > nums[j]:
                    len_num[i] += len_num[j]
            if len_num[i] == 0:
                len_num[i] = 1
            print(dp,len_num)
        max_len = max(dp)
        if max_len == 1:
            return n
        ans = 0
        for i in range(n):
            if dp[i] == max_len:
                ans += len_num[i]
        return ans

if __name__ == "__main__":
    S = Solution()
    print(S.findNumberOfLIS([3,1,2]))
