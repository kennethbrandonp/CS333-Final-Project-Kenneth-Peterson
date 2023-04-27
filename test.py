# Kenneth Peterson
# CS 333
# 04/20/23
# test.py

import unittest
from Game import Connect4Game
from Board import Connect4Board

class ConnectFourTest(unittest.TestCase):
    def setUp(self):
        self.connectGameTest = Connect4Game()       #Creates both game and board
        self.connectBoardTest = Connect4Board()

    def test_no_winner_yet(self):       #Unittests for no winner found
        self.assertFalse(self.connectGameTest.play(0))
        pass

    def test_check_no_win(self):        #Unittests for no winning condition
        self.assertFalse(self.connectBoardTest.checkWin(0,0,1))

    def test_player_swap(self):         #Unittest for swapping player
        player1 = self.connectGameTest.gameBoard.player

        player2 = self.connectGameTest.swapPlayer()

        self.assertNotEqual(player1, player2)
        pass

    def test_valid_position(self):      #Unittest for checking if there's a valid position
        row_available = self.connectGameTest.gameBoard.dropPiece(0)
        self.assertTrue(self.connectGameTest.validMove(row_available))
        pass

    def test_invalid_position(self):    #Unittest for checking if there's a invalid position
        self.connectGameTest.gameBoard.board = [[2, 0, 0, 0, 0, 0, 0],
                                            [1, 0, 0, 0, 0, 0, 0], 
                                            [2, 0, 0, 0, 0, 0, 0], 
                                            [1, 0, 0, 0, 0, 0, 0], 
                                            [2, 0, 0, 0, 0, 0, 0], 
                                            [1, 0, 0, 0, 0, 0, 0]] 
        row_not_available = self.connectGameTest.gameBoard.dropPiece(0)
        self.assertFalse(self.connectGameTest.validMove(row_not_available))
        pass

    def test_shown_board(self):     #Unittests when our board is shown to the terminal
        self.assertTrue(self.connectGameTest.showBoard(self.connectGameTest.gameBoard.board))

    def test_dropPiece(self):  #Integration test between class game and class board is satisfied when play() in class game can be used to dropPiece() on the board.
        board_with_no_entries = self.connectBoardTest.board     #Board to be compared with (Empty)

        board_with_dropped_piece = self.connectGameTest.gameBoard.board     #Board with dropped piece (Dropped piece)
        self.connectGameTest.play(0)

        self.assertNotEqual(board_with_no_entries, board_with_dropped_piece)
        pass

    def test_player1_win(self):     #Intergration test between class game and class board is satisfied when a vertical win condition is met for player 1
        self.connectGameTest.gameBoard.board = [[0, 0, 0, 0, 0, 0, 0], #This is our board, 0's mark empty slot.
                                            [0, 0, 0, 0, 0, 0, 0], 
                                            [0, 0, 0, 0, 0, 0, 0], 
                                            [1, 0, 0, 0, 0, 0, 0], 
                                            [1, 0, 0, 0, 0, 0, 0], 
                                            [1, 0, 0, 0, 0, 0, 0]] #One move away from winning for player 1
        self.assertTrue(self.connectGameTest.play(0))
        self.connectGameTest.showBoard(self.connectGameTest.gameBoard.board)
        print("Player 1 wins this test\n")
        pass

    def test_player2_win(self):     #Intergration test between class game and class board is satisfied when a  vertical win condition is met for player 2
        self.connectGameTest.gameBoard.board = [[0, 0, 0, 0, 0, 0, 0], #This is our board, 0's mark empty slot.
                                            [0, 0, 0, 0, 0, 0, 0], 
                                            [0, 0, 0, 0, 0, 0, 0], 
                                            [2, 0, 0, 0, 0, 0, 0], 
                                            [2, 0, 0, 0, 0, 0, 0], 
                                            [2, 0, 0, 0, 0, 0, 0]] #One move away from winning for player 2
        self.connectGameTest.gameBoard.player = 2
        self.assertTrue(self.connectGameTest.play(0))   #True if win condition is met
        self.connectGameTest.showBoard(self.connectGameTest.gameBoard.board)
        print("Player 2 wins this test\n")
        pass

    def test_win_horizontal(self):      #Integration test between class game and class board where a horizontal win condition is met
        self.connectGameTest.gameBoard.board = [[0, 0, 0, 0, 0, 0, 0], #This is our board, 0's mark empty slot.
                                            [0, 0, 0, 0, 0, 0, 0], 
                                            [0, 0, 0, 0, 0, 0, 0], 
                                            [0, 0, 0, 0, 0, 0, 0], 
                                            [0, 0, 0, 0, 0, 0, 0], 
                                            [0, 1, 1, 1, 0, 0, 0]] 
        
        self.assertTrue(self.connectGameTest.play(0))
        pass

    def test_win_diagonal_up_right(self):       #Integration test between class game and class board where a up-right diagonal win condition is met
        self.connectGameTest.gameBoard.board = [[0, 0, 0, 0, 0, 0, 0], #This is our board, 0's mark empty slot.
                                            [0, 0, 0, 0, 0, 0, 0], 
                                            [0, 0, 0, 1, 0, 0, 0], 
                                            [0, 0, 1, 0, 0, 0, 0], 
                                            [0, 1, 0, 0, 0, 0, 0], 
                                            [0, 0, 0, 0, 0, 0, 0]] 
        
        self.assertTrue(self.connectGameTest.play(0))
        pass

    def test_win_diagonal_down_right(self):       #Integration test between class game and class board where a down-right diagonal win condition is met
        self.connectGameTest.gameBoard.board = [[0, 0, 0, 0, 0, 0, 0], #This is our board, 0's mark empty slot.
                                            [0, 0, 0, 0, 0, 0, 0], 
                                            [1, 0, 0, 0, 0, 0, 0], 
                                            [0, 1, 0, 0, 0, 0, 0], 
                                            [0, 0, 1, 0, 0, 0, 0], 
                                            [0, 0, 0, 0, 0, 0, 0]] 
        
        self.assertTrue(self.connectGameTest.play(3))
        pass