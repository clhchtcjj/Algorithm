# -*- coding: utf-8 -*-
__author__ = 'CLH'

# 丑数
# 利用空间换时间
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        ugly_number = [1]
        p_two = p_three = p_five = 0
        while len(ugly_number)< index:
            next_ugly_number = min(2*ugly_number[p_two],3*ugly_number[p_three],5*ugly_number[p_five])
            ugly_number.append(next_ugly_number)
            # 更新三个指针
            while ugly_number[p_two]*2 <= next_ugly_number:
                p_two += 1
            while ugly_number[p_three]*3 <= next_ugly_number:
                p_three += 1
            while ugly_number[p_five]*5 <= next_ugly_number:
                p_five += 1
        return ugly_number[-1]

if __name__ == "__main__":
    S = Solution()
    S.GetUglyNumber_Solution(5)