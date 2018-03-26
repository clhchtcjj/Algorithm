__author__ = 'CLH'

'''
    # 求出模糊数字的全排列，逐个插入，求顺序对（新顺序对=旧顺序对+新产生的顺序对）
'''
class Solution():
    def __init__(self,n,k,nums):
        self.ans = []
        self.total_ans = []
        self.sum = 0
        self.nums = nums
        self.n = n
        self.k = k
        self.pos = []

    def get_pos(self):
        for i in range(0,len(self.nums)):
            if self.nums[i] == 0:
                self.pos.append(i)

    def get_mohu_nums(self):
        self.mohu_nums = []
        for i in range(1,self.n+1):
            if i not in self.nums:
                self.mohu_nums.append(i)

    def full_set(self):
        self.backtrack(0)
        # print(self.total_ans)

    def backtrack(self,k):
        if k == len(self.mohu_nums):
            self.total_ans.append(list(self.ans))
        else:
            candidates = list(set(self.mohu_nums).difference(set(self.ans)))
            for item in candidates:
                self.ans.append(item)
                self.backtrack(k+1)
                self.ans.pop()

    def count(self):
        for i in range(self.n):
            if self.nums[i] == 0:
                continue
            for j in range(i+1,self.n):
                if self.nums[i] < self.nums[j] and self.nums[j] != 0:
                    self.sum += 1

    def add_count(self,pos,num):
        # 向左
        for i in range(0,pos):
            if self.nums[i] == 0:
                continue
            if self.nums[i] < num:
                self.sum += 1
                if self.sum > self.k:
                    return -1
        for i in range(pos+1,len(self.nums)):
            if self.nums[i] == 0:
                continue
            if num < self.nums[i]:
                self.sum += 1
                if self.sum > self.k:
                    return -1
        else:
            return 1

    def get_answer(self):
        self.get_pos()
        self.get_mohu_nums()
        self.full_set()
        self.count()
        cnt = 0
        back_up = list(self.nums)
        back_sum = self.sum
        for tmp in self.total_ans:
            self.nums = list(back_up)
            self.sum = back_sum
            for i in range(len(self.pos)):
                flag = self.add_count(self.pos[i],tmp[i])
                self.nums[self.pos[i]] = tmp[i]
                if flag == -1:
                    break
            if self.sum == self.k:
                cnt+=1
        return cnt

if __name__ == "__main__":
    n,k = [int(item) for item in input().strip().split(" ")]
    nums = [int(item) for item in input().strip().split(" ")]
    S = Solution(n,k,nums)
    print(S.get_answer())




