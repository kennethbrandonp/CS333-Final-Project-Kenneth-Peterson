# Kenneth Peterson
# CS 333
# 04/20/23
# FinalProject.py

import unittest
from Game import Connect4Game


if __name__ == "__main__":
    game = Connect4Game()    #Creates game/board

    while True:
        game.showBoard(game.gameBoard.board)
        
        if game.gameBoard.player == 1:     
            print("Player 1's turn (X)")    
        else:
            print("Player 2's turn (O)")
        col = int(input("Drop piece in columns 1-7: ")) - 1     #Grabs player entry
        

        winner = game.play(col)
        if winner != False:     #Handles winner
            game.showBoard(game.gameBoard.board)
            if winner == 1:
                print("Player 1 (X) wins!")
            else:
                print("Player 2 (O) wins!")
            break       #Ends while statements
        