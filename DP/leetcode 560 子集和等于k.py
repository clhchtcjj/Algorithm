# -*- coding:utf-8-*-
__author__ = 'CLH'


class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 超时
        # n = len(nums)
        # if n == 0:
        #     return 0
        # sums = list(nums)
        # ans = 0
        # for lens in range(2, n+1):
        #     for i in range(0, n-lens+1):
        #         sums[i] += nums[i+lens-1]
        #         if sums[i] == k:
        #             ans += 1
        # return ans
        # 还超时，崩溃
        # n = len(nums)
        # if n == 0:
        #     return 0
        # ans = 0
        # sums = [0 for _ in range(n+1)]
        # for i in range(0,n):
        #     sums[i+1] = sums[i] + nums[i]
        # for i in range(n):
        #     for j in range(i+1, n+1):
        #         if sums[j]-sums[i] == k:
        #             ans += 1
        # return ans
        # 用hashmap
        sums, res, sm = {}, 0, 0
        for i in range(len(nums)):
            sums[sm], sm = sm in sums and sums[sm] + 1 or 1, sm + nums[i]
            if sm - k in sums: res += sums[sm - k]
        return res

if __name__ == "__main__":
    S = Solution()
    print(S.subarraySum([1,2,3],3))

