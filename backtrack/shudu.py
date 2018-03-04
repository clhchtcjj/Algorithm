# -- coding: utf-8 --

__author__ = 'CLH'

import math

'''
求解数独游戏
'''

class solution(object):
    def __init__(self,board):
        self.board = board

    def is_a_solution(self):
        return self.is_end()

    def process_solution(self):
        for i in range(0,9):
            for j in range(0,9):
                if (j+1) % 9 != 0:
                    print(self.board[i][j],end=" ")
                else:
                    print(self.board[i][j],end="\n")

    def construct_candidates(self, x, y):
        # 逐行遍历，得到下一个未填位置
        for next_y in range(y+1,9):
            if self.board[x][next_y] == 0:
                return x, next_y
        for next_x in range(x+1,9):
            for next_y in range(0,9):
                if self.board[next_x][next_y] == 0:
                    return next_x, next_y
        return -1,-1

    def check_fill(self,x,y,value):
        # 检查所填数值是否符合要求：行、列、宫都无重复项
        # 检查行
        for row_item in self.board[x]:
            if row_item == value:
                return False
        # 检查列
        for row_items in self.board:
            if row_items[y] == value:
                return False
        # 检查宫
        # 获得宫的位置
        start_row = int(math.floor(x / 3) * 3)  # python3.x 需要向下取整
        start_col = int(math.floor(y / 3) * 3)
        # print(x,y,start_row,start_col)
        for i in range(start_row, start_row+3):
            for j in range(start_col, start_col+3):
                if self.board[i][j] == value:
                    return False
        return True

    def is_end(self):
        for i in range(0,9):
            for j in range(0,9):
                if self.board[i][j] == 0:
                    return False
        return True

    def backtrack(self, x, y):
        if self.board[x][y] == 0:
            for i in range(1, 10):  # 从1-9开始尝试
                if self.check_fill(x, y, i):
                    self.board[x][y] = i
                    if self.is_a_solution():
                        self.process_solution()
                    next_x, next_y = self.construct_candidates(x, y)
                    if next_x == -1:
                        return
                    else:
                        self.backtrack(next_x, next_y)
                        end = self.is_end()
                        if end is False:
                            self.board[x][y] = 0
                        else:
                            return

    def fill(self):
        num_fill = 0
        for i in range(0,9):
            for j in range(0,9):
                if self.board[i][j] == 0:
                    num_fill += 1
        if self.board[0][0] == 0:
            self.backtrack(0,0)
        else:
            next_x, next_y = self.construct_candidates(0,0)
            self.backtrack(next_x,next_y)
        # for i in self.board:
        #     print(i)

if __name__ == "__main__":
    s = solution([[8,0,0,0,0,0,0,0,0],
        [0,0,3,6,0,0,0,0,0],
        [0,7,0,0,9,0,2,0,0],
        [0,5,0,0,0,7,0,0,0],
        [0,0,0,8,4,5,7,0,0],
        [0,0,0,1,0,0,0,3,0],
        [0,0,1,0,0,0,0,6,8],
        [0,0,8,5,0,0,0,1,0],
        [0,9,0,0,0,0,4,0,0]])
    s.fill()