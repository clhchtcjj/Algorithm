# -*- coding:utf-8 -*-
__author__ = 'CLH'

class Solution:
    def __init__(self):
        self.ans = []
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        else:
            nums = list(ss)
            self._Premutation(nums,0)
            return sorted(self.ans)

    def _Premutation(self,nums,k):
        if k == len(nums)-1:
            self.ans.append(''.join(nums))
        else:
            for i in range(k,len(nums)):
                # print(nums)
                if nums[i] == nums[k] and i!=k:
                    continue
                nums[i],nums[k]= nums[k],nums[i]
                self._Premutation(nums,k+1)
                nums[i],nums[k] = nums[k],nums[i]

if __name__ == "__main__":
    S = Solution()
    print(S.Permutation("abc"))