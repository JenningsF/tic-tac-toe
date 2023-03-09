import os

class GameBoard:
    def __init__(self):
        self.board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    
    def __str__(self):
        os.system("cls")
        board_print = "\n"
        print(board_print)
        # print("\n")
        for num in range(1,len(self.board)):
            # print(f"Step{num - 1}: {board_print}")
            if num < 4:
                index = num + 6
                board_print += f"{self.board[index]} "
            elif num > 6:
                index = num - 6
                board_print += f"{self.board[index]} "
                # print(self.board[index], end = " ")
            else:
                board_print += f"{self.board[num]} "
                # print(self.board[num], end = " ")

            if num % 3 != 0:
                board_print += "| "
            if num < 9 and num % 3 == 0:
                board_print += "\n---------\n"
        board_print += "\n"
        # print(board_print)
        return board_print

    # Take board, marker ('X' or 'O') and position number and assigns it to the board
    def place_marker(self, marker, position):
        self.board[position] = marker

    # Returns whether selected space is available
    def is_open_position(self, position):
        is_open = self.board[position] == " "
        return self.board[position] == " "

    # Checks if board is full
    def full_board_check(self):
        return ' ' in self.board

    # Checks if a player has won after marker is placed
    def win_check(self):
        is_winning_move = False

        # Vertical Checks
        if self.board[7] == self.board[4] == self.board[1] == 'X' or self.board[7] == self.board[4] == self.board[1] == 'O':
            is_winning_move = True
        elif self.board[8] == self.board[5] == self.board[2] == 'X' or self.board[8] == self.board[5] == self.board[2] == 'O':
            is_winning_move = True
        elif self.board[9] == self.board[6] == self.board[3] == 'X' or self.board[9] == self.board[6] == self.board[3] == 'O':
            is_winning_move = True

        # Horizontal Checks
        if self.board[7] == self.board[8] == self.board[9] == 'X' or self.board[7] == self.board[8] == self.board[9] == 'O':
            is_winning_move = True
        elif self.board[4] == self.board[5] == self.board[6] == 'X' or self.board[4] == self.board[5] == self.board[6] == 'O':
            is_winning_move = True
        elif self.board[1] == self.board[2] == self.board[3] == 'X' or self.board[1] == self.board[2] == self.board[3] == 'O':
            is_winning_move = True
        # Diagonal Checks
        if self.board[7] == self.board[5] == self.board[3] == 'X' or self.board[7] == self.board[5] == self.board[3] == 'O':
            is_winning_move = True
        elif self.board[9] == self.board[5] == self.board[1] == 'X' or self.board[9] == self.board[5] == self.board[1] == 'O':
            is_winning_move = True

        return is_winning_move
