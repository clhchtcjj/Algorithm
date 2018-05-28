# -*- coding: utf-8 -*-
__author__ = 'CLH'

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 0:
            return False
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        else:
            half_sum = int(total_sum // 2)
            dp = [False for _ in range(half_sum+1)]
            dp[0] = True
            for i,num in enumerate(nums):
                last_dp = list(dp)
                for j in range(num,half_sum+1):
                    dp[j] = last_dp[j] or last_dp[j-num]
                print(dp)
            return dp[-1]



if __name__ == "__main__":
    S = Solution()
    print(S.canPartition([1,2,5]))




