# -*- coding:utf-8 -*-
__author__ = 'CLH'

# 把数组排成最小数
# 思路：比较两个元素，交换与不交换位置，拼接起来谁大
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if len(numbers) == 0:
            return ""
        numbers.sort(cmp = lambda x,y: cmp(str(x) + str(y), str(y) + str(x)))
        string = ""
        for num in numbers:
            string+=str(num)
        return string

if __name__ == "__main__":
    S = Solution()
    print(S.PrintMinNumber([1]))