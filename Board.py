# Kenneth Peterson
# CS 333
# 04/20/23
# Board.py

class Connect4Board:
    def __init__(self):
        self.rows = 6 
        self.cols = 7
        self.board = [[0, 0, 0, 0, 0, 0, 0], #This is our board, 0's mark empty slot
                      [0, 0, 0, 0, 0, 0, 0], 
                      [0, 0, 0, 0, 0, 0, 0], 
                      [0, 0, 0, 0, 0, 0, 0], 
                      [0, 0, 0, 0, 0, 0, 0], 
                      [0, 0, 0, 0, 0, 0, 0]] 
        self.player = 1     #The player switches from 1 (X) and 2 (O)

    def dropPiece(self, col):
        row = self.rows - 1
        while row >= 0:
            if self.board[row][col] == 0:
                self.board[row][col] = self.player
                return row      #Number of available rows left
            row -= 1

        return None  #Returns None if no rows available


    def checkWin(self, row, col, player):
        #Horizontal win
        count = 0
        for c in range(col - 3, col + 4):
            if c >= 0 and c < self.cols and self.board[row][c] == player:
                count += 1
                if count == 4:  
                    return True

        #Vertical win
        count = 0
        for r in range(row - 3, row + 4):
            if r >= 0 and r < self.rows and self.board[r][col] == player:
                count += 1
                if count == 4:
                    return True

        #Diagonal win (down-right)
        count = 0
        for i in range(-3, 4):
            r = row + i
            c = col + i
            if r >= 0 and r < self.rows and c >= 0 and c < self.cols and self.board[r][c] == player:
                count += 1
                if count == 4:
                    return True

        #Diagonal win (up-right)
        count = 0
        for i in range(-3, 4):
            r = row - i
            c = col + i
            if r >= 0 and r < self.rows and c >= 0 and c < self.cols and self.board[r][c] == player:
                count += 1
                if count == 4:
                    return True

        return False    #No win condition met