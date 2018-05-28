# -*- coding:utf-8 -*-
__author__ = 'CLH'


class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        if n < k:
            return False
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        partition_sum = total_sum // k

        def dfs(nums, visited, target, curr_sum, s, k):
            if k == 1:
                return True
            if curr_sum == target:
                return dfs(nums,visited,target,0,0,k-1)
            for i in range(s,len(nums)):
                if visited[i] == 0:
                    visited[i] = 1
                    if dfs(nums,visited,target,curr_sum+nums[i],i+1,k):
                        return True
                    visited[i] = 0
            return False
        visited = [0 for _ in range(n)]
        return dfs(nums,visited,partition_sum,0,0,k)

if __name__ == "__main__":
    nums = [780,935,2439,444,513,1603,504,2162,432,110,1856,575,172,367,288,316]
    S = Solution()
    print(S.canPartitionKSubsets(nums,k=4))