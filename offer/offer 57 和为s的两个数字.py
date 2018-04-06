# -*- coding: utf-8 -*-
__author__ = 'CLH'

# 排序数组
# 两个数 => 定义两个指针，
# 一头一尾，看加起来的和与目标值的关系，大于目标值，尾巴向前走；小于目标值，头向后走
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []
        tmp = sorted(nums)
        head = 0
        tail = n-1
        while head < tail:
            two_sum = nums[head] + nums[tail]
            if two_sum == target:
                index_1 = nums.index(nums[head])
                nums[index_1] = None
                return [index_1,nums.index(tmp[tail])]
            if two_sum < target:
                head += 1
            else:
                tail -= 1
        return []

