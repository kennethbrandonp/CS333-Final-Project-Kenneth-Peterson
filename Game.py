# Kenneth Peterson
# CS 333
# 04/20/23
# Game.py

from Board import Connect4Board

class Connect4Game:
    def __init__(self, gameBoard = None):
        if gameBoard is None:       #If we aren't given an already saved board, make a fresh and empty board
            self.gameBoard = Connect4Board()
        else:               #Otherwise use the one provided
            self.gameBoard = gameBoard

    def play(self, col):
        row = self.gameBoard.dropPiece(col)    #Drops piece in column selected
        self.validMove(row)        #Checks for valid move

        if self.gameBoard.checkWin(row, col, self.gameBoard.player) == True:    #If the row has entries, check if there's a win
            return True

        self.swapPlayer()       #No wins means swap player
        return False
    
    def swapPlayer(self):
        if self.gameBoard.player == 1:      #If it was player 1's turn, swap to 2
            self.gameBoard.player = 2
            return self.gameBoard.player
        
        if self.gameBoard.player == 2:      #If it was player 2's turn, swap to 1
            self.gameBoard.player = 1
            return self.gameBoard.player

    def validMove(self, row):       #For unittesting purposes
        if row != None:     #Row has available spaces
            return True
        else:               #Row is completely full
            print("\n*** Invalid Move, try any of the remaining slots ***")
            return False

    def showBoard(self, board):
        for row in board:
            print("|", end = "")
            for slot in row:
                if slot == 1:
                    print("X", end = "|")   #Displays player 1's current moves

                elif slot == 2:
                    print("O", end = "|")   #Displays player 2's current moves

                else:
                    print(" ", end = "|")   #Shows available spaces
            print()
        return True