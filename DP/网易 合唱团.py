
class Solution():
    def __init__(self,n,k,d,nums):
        # dp[i][j]:以第i个人结尾时，合唱团有j+1个人时的能力值乘积
        self.dp_min = [[0 for i in range(k)] for j in range(n)]
        self.dp_max = [[0 for i in range(k)] for j in range(n)]
        self.nums = nums
        self.d = d
     
    def dp(self,n,k,d,nums):
        # 保存记录最大值
        max_value = 0
        # 初始化，当合唱团只有一个人时
        for i in range(n):
            self.dp_min[i][0] = nums[i]
            self.dp_max[i][0] = nums[i]
        for i in range(n):
            for j in range(1,k):
                for p in range(i-1,max(-1,i-d-1),-1):
                    self.dp_max[i][j] = max(self.dp_max[i][j],max(self.dp_max[p][j-1]*self.nums[i], self.dp_min[p][j-1]* nums[i]))
                    self.dp_min[i][j] = min(self.dp_min[i][j],min(self.dp_max[p][j-1]*self.nums[i], self.dp_min[p][j-1]* nums[i]))
            if max_value < self.dp_max[i][k-1]:
                max_value = self.dp_max[i][k-1]
        return max_value
            

if __name__ == "__main__":
    n = int(input())
    nums = [int(item) for item in input().strip().split(" ")]
    k,d =  [int(item) for item in input().strip().split(" ")]
    S = Solution(n,k,d,nums)
    print(S.dp(n,k,d,nums))