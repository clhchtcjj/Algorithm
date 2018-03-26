__author__ = 'CLH'

# 用两个栈实现队列


class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack1.append(x)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.stack2) != 0:
            return self.stack2.pop()
        else:
            for i in range(len(self.stack1)-1,-1,-1):
                self.stack2.append(self.stack1[i])
            self.stack1 = []
            return self.stack2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.stack2) != 0:
            return self.stack2[-1]
        else:
            for i in range(len(self.stack1)-1,-1,-1):
                self.stack2.append(self.stack1[i])
            self.stack1 = []
            return self.stack2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return True
        else:
            return False



# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_2 = obj.peek()
param_3 = obj.peek()
param_4 = obj.empty()
print(param_2,param_3,param_4)