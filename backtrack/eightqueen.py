__author__ = 'CLH'

'''
    八皇后
'''


class solution(object):
    def __init__(self,board,num_queen):
        self.board = board
        self.num_queen = num_queen
        self.num_answer = 0

    def is_a_solution(self,k):
        return k ==  self.num_queen

    def process_solution(self):
        for row in self.board:
            print(row)
        self.num_answer += 1
        print(self.num_answer)

    def check_fill(self,x,y):
        # 检查行
        if 1 in self.board[x]:
            return False
        # 检查列
        for row in self.board:
            if row[y] == 1:
                return False
        # 检查对角线
        temp_x = x
        temp_y = y
        while(temp_x-1) > -1 and (temp_y-1) >-1:
            temp_x = temp_x - 1
            temp_y = temp_y - 1
            if self.board[temp_x][temp_y] == 1:
                return False
        temp_x = x
        temp_y = y
        while(temp_x-1) > -1 and (temp_y+1) < self.num_queen:
            temp_x = temp_x - 1
            temp_y = temp_y + 1
            if self.board[temp_x][temp_y] == 1:
                return False
        temp_x = x
        temp_y = y
        while(temp_x+1) < self.num_queen and (temp_y-1) > -1:
            temp_x = temp_x + 1
            temp_y = temp_y - 1
            if self.board[temp_x][temp_y] == 1:
                return False
        temp_x = x
        temp_y = y
        while(temp_x+1) < self.num_queen and (temp_y+1) < self.num_queen:
            temp_x = temp_x + 1
            temp_y = temp_y + 1
            if self.board[temp_x][temp_y] == 1:
                return False
        return True

    def construct_candidates(self, x):
        candidates = []
        for i in range(self.num_queen):
            if self.check_fill(x, i):
                candidates.append(i)
        return candidates

    def backtrack(self, k):
        if self.is_a_solution(k):
            self.process_solution()
        else:
            k = k + 1
            candidates = self.construct_candidates(k-1)
            for y in candidates:
                self.board[k-1][y] = 1
                self.backtrack(k)
                self.board[k-1][y] = 0
                if k == self.num_queen:
                    return

if __name__ == "__main__":
    num_queen = 8
    board = []
    for i in range(num_queen):
        board.append([0]*num_queen)
    s = solution(board,num_queen)
    s.backtrack(0)

