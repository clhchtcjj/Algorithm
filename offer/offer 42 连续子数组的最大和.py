# -*- coding:utf-8 -*-
__author__ = 'CLH'

# 连续子数组的最大和
# 思路：维护两个变量，当前最大和、和
# 如果加上自己，没有自己本身大，则丢弃之前的累加值，更新为自己本身
# 更新当前最大和

class Solution():
    def FindGreatestSumOfSubArray(self, array):
        if len(array) == 0:
            return -1
        # write code herecc
        max_sum = - float('inf')
        add_sum = 0
        for num in array:
            if add_sum + num < num:
                add_sum = num
            else:
                add_sum += num
            if max_sum < add_sum:
                max_sum = add_sum

        return max_sum

    def dpFind(self,array):
        f = [0] * len(array)
        f[0] = array[0]
        max_sum = f[0]
        for i in range(1,len(array)):
            if f[i-1] <= 0:
                f[i] = array[i]
            else:
                f[i] = array[i] + f[i-1]
            if max_sum < f[i]:
                max_sum = f[i]
        return max_sum

if __name__ == "__main__":
    S = Solution()
    print(S.dpFind([6,-3,-2,7,-15,1,2,2]))


