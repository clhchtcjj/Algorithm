__author__ = 'CLH'

from queue import Queue

class Solution():
    def __init__(self,n,m,board,k,steps,x0,y0):
        self.board = board # 地牢
        self.k = k  #最大步数
        self.steps = steps # 每次课移动的步数
        self.x0 = x0
        self.y0 = y0
        self.dis = [[0 for j in range(m)] for i in range(n)]
        self.n = n
        self.m = m


    def BFS(self):
        queue_x = Queue()
        queue_y = Queue()
        queue_x.put(self.x0)
        queue_y.put(self.y0)
        self.dis[self.x0][self.y0] = 1
        while not queue_x.empty() and not queue_y.empty():
            x = queue_x.get()
            y = queue_y.get()
            for i in range(self.k):
                new_x = x + self.steps[i][0]
                new_y = y + self.steps[i][1]
                if 0 <= new_x and new_x < self.n and 0 <= new_y and new_y < self.m:
                    if self.dis[new_x][new_y] == 0:
                        if  self.board[new_x][new_y] == '.':
                            queue_x.put(new_x)
                            queue_y.put(new_y)
                            self.dis[new_x][new_y] = self.dis[x][y] + 1
                        else:
                            self.dis[new_x][new_y] = -1


    def escape(self):
        self.BFS()
        max_steps = 0
        fail = False
        for i in range(self.n):
            for j in range(self.m):
                if self.dis[i][j] == 0 and self.board[i][j] == '.':
                    fail = True
                max_steps = max(max_steps,self.dis[i][j])
        if fail == True:
            return -1
        else:
            return max_steps-1


if __name__ == "__main__":
    n,m = [int(item) for item in input().strip().split(" ")]
    board = []
    for i in range(n):
        tmp = list(input().strip())
        board.append(tmp)
    x0,y0 = [int(item) for item in input().strip().split(" ")]
    k = int(input())
    steps = []
    for i in range(k):
        tmp = [int(item) for item in input().strip().split(" ")]
        steps.append(tmp)
    S = Solution(n,m,board,k,steps,x0,y0)
    print(S.escape())




