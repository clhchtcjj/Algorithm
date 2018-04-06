# -*- coding:utf-8 -*-
__author__ = 'CLH'
# 序列数字中某一位的值
# 找规律：1-9 ： 9 位
#         10-99： 90 位
#         100-999: 900 位

class Solution():

    def getNumber(self,index):
        if index < 0:
            return -1
        else:
            digits = 1
            while True:
                counts = self.countOfInteger(digits)
                if index < counts:
                    return self.digitAtIndex(index,digits)
                index -= digits * counts
                digits += 1

    def digitAtIndex(self,index,digits):
        number = self.beginNumber(digits) + index / digits
        index_from_right = digits - index % digits
        for i in range(1,index_from_right):
            number /= 10
        return number%10
    def beginNumber(self,digits):
        if digits == 1:
            return 0
        else:
            return pow(10,digits-1)


    def countOfInteger(self, digits):
        if digits == 1:
            return 9
        else:
            return 9 * pow(10, digits)