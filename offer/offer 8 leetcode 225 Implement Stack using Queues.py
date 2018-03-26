__author__ = 'CLH'

# 利用队列实现栈
import Queue

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = Queue.Queue()
        self.queue2 = Queue.Queue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue1.put(x)


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        tmp = None
        if self.queue2.empty():
            while self.queue1.qsize() > 1:
                self.queue2.put(self.queue1.get())
            tmp = self.queue1.get()
            while not self.queue2.empty():
                self.queue1.put(self.queue2.get())
        return tmp



    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        tmp = None
        if self.queue2.empty():
            while not self.queue1.empty():
                tmp = self.queue1.get()
                self.queue2.put(tmp)
            while not self.queue2.empty():
                self.queue1.put(self.queue2.get())
        return tmp

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if self.queue1.empty() and self.queue2.empty():
            return True
        else:
            return False



# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
param_2 = obj.pop()
obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
print(param_2,param_3,param_4)
