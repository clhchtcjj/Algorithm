__author__ = 'CLH'

'''
    给定无重复数字的数组，求其子集
'''

class Solution(object):
    def __init__(self):
        self.ans = []
        self.total_ans = []
        self.nums = []

    def process_solution(self):
        nums = []
        for i in range(len(self.ans)):
            if self.ans[i] == 1:
                nums.append(self.nums[i])
        self.total_ans.append(nums)

    def backtrack(self,k):
        if k == len(self.nums):
            self.process_solution()
        else:
            for i in [0,1]:
                self.ans.append(i)
                self.backtrack(k+1)
                self.ans.pop()

    #
    #
    #
    # def subsets(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     self.nums = nums
    #     self.backtrack(0)
    #     return self.total_ans
# 简单解法
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        total_ans = [[]]
        for num in nums:
            total_ans += [item + [num] for item in total_ans]
        return total_ans

if __name__ == "__main__":
    S = Solution()
    print(S.subsets([1,5,3,4]))