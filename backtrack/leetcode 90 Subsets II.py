__author__ = 'CLH'

'''
    Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
'''


class TireNode():
    def __init__(self):
        self.childs = {}
        self.is_subset = False


class Solution:
    def __init__(self):
        self.tire = TireNode()
        self.ans = []
        self.total_ans = []
        self.nums = []
        self.none = False

    def add(self,nums):
        node = self.tire
        for num in nums:
            if node.childs.get(num) is None:
                node.childs[num] = TireNode()
            node = node.childs[num]
        node.is_subset = True

    def search(self,nums):
        node = self.tire
        for num in nums:
            if node.childs.get(num) is None:
                return False
            node = node.childs[num]
        return node.is_subset

    def process_solution(self):
        nums = []
        for i in range(len(self.ans)):
            if self.ans[i] == 1:
                nums.append(self.nums[i])
        if len(nums) == 0 and self.none == False:
            self.total_ans.append(nums)
        else:
            # 集合是无序的，为了防止将元素相同的子集添加进tire，可以先拍个序，再进行插入、查找
            sorted_nums = sorted(nums)
            if not self.search(sorted_nums):
                self.total_ans.append(nums)
                self.add(sorted_nums)


    def backtrack(self,k):
        if k == len(self.nums):
            self.process_solution()
        else:
            # 每个num只有放和不放两种可能
            for i in range(2):
                self.ans.append(i)
                self.backtrack(k+1)
                self.ans.pop()




    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = nums
        self.backtrack(0)
        return self.total_ans


if __name__ == "__main__":
    S = Solution()
    print(S.subsetsWithDup([4,4,4,1,4]))

