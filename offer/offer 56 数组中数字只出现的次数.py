# -*- coding:utf-8 -*-
__author__ = 'CLH'

# 数组中数字值出现的次数

class Solution(object):
    def singleNumber_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        某一数字只出现了一次，其他的出现了2次，找出该数字
        两次 ==>xor后为0
        """
        if len(nums) == 0:
            return None
        sum = nums[0]
        for num in nums[1:]:
            sum ^= num
        return sum


    def singleNumber_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        某一数字只出现了一次，其他的出现了3次，找出该数字
        三次 ==> 按照位相加，能被三整除
        """
        if len(nums) == 0:
            return None
        bitSum = [0] * 32
        for i in range(0,len(nums)):
            bitMask = 1
            for j in range(31,-1,-1):
                print(bitMask)
                bit = nums[i] & bitMask
                if bit != 0:
                    bitSum[j] += 1
                bitMask = bitMask << 1

        result = 0
        for i in range(0,32):
            result = result << 1
            result += bitSum[i] % 3
        return self.convert(result)

    def convert(self,x):
        if x >= 2**31:
            x -= 2**32
        return x

    def singleNumber_3(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        分组，将两个出现一次的数分到不同组
        """
        if len(nums) == 0:
            return None
        sum = nums[0]
        for num in nums[1:]:
            sum ^= num
        bit_1 = -1
        while sum:
            bit = sum & 1
            bit_1 += 1
            if bit == 1:
                break
            sum >>= 1
        nums_1 = []
        nums_2 = []
        for num in nums:
            if (num >> bit_1) & 1 == 1:
                nums_1.append(num)
            else:
                nums_2.append(num)
        # if len(nums_1) == 0 or len(nums_2)==0:
        #     return nums
        a = nums_1[0]
        b = nums_2[0]
        for num in nums_1[1:]:
            a ^= num
        for num in nums_2[1:]:
            b ^= num
        return [a,b]

if __name__ == "__main__":
    S = Solution()
    print(S.singleNumber_3([0,1]))





# if __name__ == "__main__":
#     S = Solution()
#     print(S.singleNumber_2([-2,-2,1,1,-3,1,-3,-3,-4,-2]))