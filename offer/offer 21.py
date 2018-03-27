# -- coding:utf-8 --
__author__ = 'CLH'

# 调整数组顺序 一半的一半
# 思路：首尾两个指针
class Solution():
    def adjustList(self,nums,func):
        '''
        前半部分奇数，后半部分偶数
        :param nums:
        :return:
        '''
        start = 0
        end = len(nums) - 1
        while start < end:
            # 找到前半部分，第一个偶数
            while start < end and func(nums[start]):
                start += 1
            # 找到后半部分，从后往前第一个奇数
            while start < end and not func(nums[end]):
                end -= 1
            if start < end:
                nums[start],nums[end] = nums[end],nums[start]
        print(start)

    def is_odd(self,num):
        return num & 1
    def is_three(self,num):
        return num % 3 == 0

if __name__ == "__main__":
    S = Solution()
    nums = [1,2,3,4,5,6,7,8]
    S.adjustList(nums,S.is_three)
    print(nums)


