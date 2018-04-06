# -*- coding:utf-8 -*-
__author__ = 'CLH'

# 逆序对

class Solution(object):

    def reversePairs(self, nums):
        if len(nums) == 0:
            return 0
        copy = list(nums)
        return self.reversePairsCore(nums,copy,0,len(nums)-1)


    def reversePairsCore(self,nums,copy,s,t):
        if s == t:
            copy[s] = nums[s]
            return 0
        lens = (t-s) // 2
        left = self.reversePairsCore(copy,nums,s,s+lens)
        right = self.reversePairsCore(copy,nums,s+lens+1,t)
        i = s
        j = s+lens+1
        cnt = 0
        while i <= s+lens and j <= t:
            if nums[i] > 2 * nums[j]:
                cnt += lens + s - i + 1
                j += 1
            else:
                i += 1
        i = s
        j = s+lens+1
        ind = s
        while i <= s+lens and j <= t:
            if nums[i] > nums[j]:
                copy[ind] = nums[j]
                ind += 1
                j += 1
            else:
                copy[ind] = nums[i]
                ind += 1
                i += 1
        while i <= s+lens:
            copy[ind] = nums[i]
            ind += 1
            i += 1
        while j <= t:
            copy[ind] = nums[j]
            ind += 1
            j += 1
        return cnt + right + left

if __name__ == "__main__":
    S = Solution()
    print(S.reversePairs([233,2000000001,234,2000000006,235,2000000003,236,2000000007,237,2000000002,2000000005,233,233,233,233,233,2000000004]))



