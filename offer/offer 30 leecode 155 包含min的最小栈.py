# -*- coding:utf-8 -*-
__author__ = 'CLH'


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.mins = []
        self.min = None


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.nums.append(x)
        if self.min is None:
            self.min = x
        elif self.min > x:
            self.min = x
        self.mins.append(self.min)


    def pop(self):
        """
        :rtype: void
        """
        if len(self.nums) == 0:
            return
        num = self.nums[-1]
        self.nums=self.nums[:-1]
        self.mins = self.mins[:-1]
        return num

    def top(self):
        """
        :rtype: int
        """
        if len(self.nums) == 0:
            return None
        return self.nums[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.mins) == 0:
            return None
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(0)
obj.push(1)
obj.push(0)
print(obj.getMin())
obj.pop()
print(obj.getMin())